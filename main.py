import os
from telegram import Update,Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
from replit import db

bot=Bot(os.environ['token'])

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('hello ! \ncommands: \n  /setup [username] -- setup the account. \n /expiry --  get expiry date')

def setup(update: Update, context: CallbackContext) -> None:
    if len(context.args)!=0:
      db[str(update.effective_message.chat_id)] = context.args[0]
      update.message.reply_text('your account is added successfully .')
def expirydate(update: Update, context: CallbackContext) -> None:
  print("f")

def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.

    
    my_secret = os.environ['token']
    updater = Updater(my_secret)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("setup", setup))
    dispatcher.add_handler(CommandHandler("expirydate", expirydate))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()