# scrapy-googlechat
Send crawl reports from Scrapy spiders to Google Chat

## Usage
Create a webhook in Google Chat: https://developers.google.com/hangouts/chat/how-tos/webhooks

Within your Scrapy project, install the package:
```bash
pip install scrapy-googlechat
```

Register and configure the extension in `settings.py`:
```python
EXTENSIONS = {
    ...
    'scrapy_google_chat.GoogleChatBot': 100,
    ...
}
...
GOOGLE_CHAT_WEBHOOK = 'YOUR_WEBHOOK'

# Optional: change the image displayed in Google Chat
GOOGLE_CHAT_IMAGE = 'https://img.icons8.com/ios/452/spider.png'
```

You're good to go. Happy crawling!
