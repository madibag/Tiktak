## [Tiktak](https://telegram.dog/etnahbot)
---

An Open Source Tiktok Telegram RoBot, that can do lot of things.
👉 check the 'branches' for all the features..!

## Credits, and Thanks to

* [Python-telegram-bot Library](https://github.com/python-telegram-bot/python-telegram-bot)
* [Authors](https://github.com/ytdl-org/youtube-dl/blob/master/AUTHORS) for their [Youtube-dl](https://github.com/ytdl-org/youtube-dl/)

### Installation

#### The Easy Way

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

#### The Hard Way

```sh
virtualenv -p python3 VENV
. ./VENV/bin/activate
pip install -r requirements.txt
# <Create config.py with variables as given below>
python bot.py
```

An example `config.py` file could be:

**Not All of the variables are mandatory**

```python3
from sample_config import Config

class Development(Config):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
  TG_BOT_TOKEN = ""
  AUTH_USERS = [
    7351948
  ]
```

### [@BotFather](https://telegram.dog/BotFather) Commands

```
start - Check if the Bot is Online!
help - How to use this Bot?
```

- For FeedBack and Suggestions, please feel free to say in [@nahom_d](https://telegram.dog/nahom_d)

#### LICENSE
- GPLv3
