#  import the modules we need
from telegram import Update
from telegram.ext import CommandHandler, Application,CallbackContext, MessageHandler,filters

# set the bot token
bot_token=" "

# /start command
async def start(update:Update,cotext:CallbackContext)->None:
    await update.message.reply_text("I am a telegram bot built with python")

# /help command
async def help_command(update:Update,context:CallbackContext)->None:
    await update.message.reply_text(
        "Here are the commands you can use:\n"
        "/start: to start the bot\n"
        "/help: to get list of commands\n"
        "/info: to get information about the bot\n"
        "/service: see what i can do!\n"
    )

# /info command
async def info_command(update:Update,context:CallbackContext)->None:(
    await update.message.reply_text("I am a Telegram automation bot built using Python! 🚀")
)
    
# /service command
async def service_command(update:Update,context:CallbackContext)->None:
    await update.message.reply_text("I can send messages, automate tasks, and more! 🤖"
                                    
)



# handle any messages
async def echo(update:Update,context:CallbackContext)->None:
    user_message=update.message.text.lower()

    if user_message=="hi":
        await update.message.reply_text("Hello!")
    elif user_message=="how are you":
        await update.message.reply_text("I'm good, thank you!")
    elif user_message=="bye":
        await update.message.reply_text("Goodbye!")
    else:
        await update.message.reply_text("I don't understand that command. Please use /help to see the list of commands.")

def main():
    application=Application.builder().token(bot_token).build()

    # add command handler
    application.add_handler(CommandHandler("start",start))
    application.add_handler(CommandHandler("help",help_command))
    application.add_handler(CommandHandler("info",info_command))
    application.add_handler(CommandHandler("service",service_command))

    # add message handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,echo))

    # start the bot
    application.run_polling()

if __name__ == '__main__':
    main()