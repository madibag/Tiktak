from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ParseMode
from down import downloader
import os
#INCONCISTENT

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

def start(update,context):
    name = update.message.chat.first_name
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id = chat_id,
        text='''Hello {} Welcome to My Tiktok
         Video Downloading Bot For more Help
         Sent \help 
         <a href='https://t.me/nahom_d'>developer<a>
        '''.format(name),
        parse_mode = ParseMode.HTML, disable_web_page_preview=True

        )
def help(update,context):
    update.message.reply_text('To download videos\nsimply paste you download link\nThen send')
def url(update,context):
    msg = update.message.text
    if msg.startswith('https://'):
        return downloader(update,context,msg)


def main():
    """Start the bot."""
    updater = Updater(Config.TG_BOT_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))


    # on noncommand i.e message - echo the message on Telegra
    dp.add_handler(MessageHandler(Filters.text, url))
    #dp.add_handler(MessageHandler(Filters.text, echo))


    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
