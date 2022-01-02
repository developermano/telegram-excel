import os
from telegram import Update,Bot
from telegram.ext import Updater, CommandHandler, CallbackContext


bot=Bot(os.environ['token'])

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('hello ! \ncommands: \n  /setup [username] -- setup the account. \n /expiry --  get expiry date')


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.

    
    my_secret = os.environ['token']
    updater = Updater(my_secret)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()