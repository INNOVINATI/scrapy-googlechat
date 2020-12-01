import json
from urllib.request import Request, urlopen

from scrapy import signals
from scrapy.exceptions import NotConfigured


class GoogleChatBot(object):
    """
    Sends crawl reports to Google Chat

    REQUIRED SETTING:
    - GOOGLE_CHAT_WEBHOOK = 'https://chat.googleapis.com/v1/spaces/XXXXXXXX/messages?key=XXXXXXXX&token=XXXXXXXX'

    Read here to learn how to create a webhook: https://developers.google.com/hangouts/chat/how-tos/webhooks

    """

    def __init__(self, url, stats, image):
        self.url = url
        self.image = image
        self.crawl_stats = stats
        self.item_stats = {'scraped': 0, 'dropped': 0, 'errors': 0}

    @classmethod
    def from_crawler(cls, crawler):
        if not (url := crawler.settings.get('GOOGLE_CHAT_WEBHOOK')):
            raise NotConfigured
        image = crawler.settings.get('GOOGLE_CHAT_IMAGE', 'https://img.icons8.com/ios/452/spider.png')
        ext = cls(url, crawler.stats, image)
        crawler.signals.connect(ext.spider_closed, signal=signals.spider_closed)
        crawler.signals.connect(ext.item_scraped, signal=signals.item_scraped)
        crawler.signals.connect(ext.item_dropped, signal=signals.item_dropped)
        crawler.signals.connect(ext.item_error, signal=signals.item_error)
        return ext

    def spider_closed(self, spider):
        self.item_stats['total'] = sum([v for k, v in self.item_stats.items() if k != 'total'])
        self.item_stats['duration'] = self._get_duration()
        msg = self._get_message(spider.name, self.item_stats)
        response = urlopen(Request(
            self.url,
            data=str.encode(json.dumps(msg)),
            headers={'Content-Type': 'application/json; charset=UTF-8'},
            method='POST'
        ))

    def item_scraped(self, item, spider):
        self.item_stats['scraped'] += 1

    def item_dropped(self, item, spider):
        self.item_stats['dropped'] += 1

    def item_error(self, item, spider):
        self.item_stats['errors'] += 1

    def _get_duration(self):
        duration = self.crawl_stats.get_value('finish_time') - self.crawl_stats.get_value('start_time')
        total_seconds = int(duration.total_seconds())
        hours, remainder = divmod(total_seconds, 60 * 60)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours}h {minutes}m {seconds}s"

    def _get_message(self, spider_name, stats):
        return {
            'cards': [
                {
                    'header': {
                        "title": "Spider Report",
                        "subtitle": f'Name: {spider_name}',
                        "imageUrl": self.image,
                        "imageStyle": "IMAGE"
                    },
                    'sections': [
                        {
                            'widgets': [{
                                'textParagraph': {
                                    'text': '<br>'.join([f'<b>{key}:</b> {value}' for key, value in stats.items()]),
                                }
                            }]
                        }
                    ]
                }
            ]
        }
