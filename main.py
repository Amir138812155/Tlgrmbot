from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text('سلام! من ربات توام!')

def main():
    updater = Updater("7523537093:AAE7YBXE5NZaANZbln6tW5g9ckiepDGrcRk", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
