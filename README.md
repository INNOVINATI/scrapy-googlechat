# scrapy-google-chat
Send crawl reports from Scrapy spiders to Google Chat

## Usage
Create a webhook in Google Chat: https://developers.google.com/hangouts/chat/how-tos/webhooks

Within your Scrapy project, install the package:
```bash
pip install scrapy-google-chat
```

Register and configure the extension in `settings.py`:
```bash
EXTENSIONS = {
    ...
    'scrapy_google_chat.GoogleChatBot': 100,
    ...
}
...
GOOGLE_CHAT_WEBHOOK = <YOUR_WEBHOOK>
```

You're good to go. Happy crawling!
