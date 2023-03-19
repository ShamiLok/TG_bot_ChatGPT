
import os
import telegram
import openai
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

load_dotenv()

BOT_TOKEN = 'API'
bot = telegram.Bot(token=BOT_TOKEN)
openai.api_key = "API"



def openai_complete(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = response.choices[0].text
    return message


def handle_message(update, context):
    message = update.message.text
    response = openai_complete(message)
    update.message.reply_text(response)


def main():
    updater = Updater(token=BOT_TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()