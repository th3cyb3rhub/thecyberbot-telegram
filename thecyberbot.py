import logging
from telegram import Bot, Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackContext,
    CallbackQueryHandler,
    MessageHandler,
    filters,
)
from dotenv import load_dotenv
import os

# gemini
import textwrap
import google.generativeai as genai
from IPython.display import Markdown

load_dotenv()

GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
Bot_Token = os.getenv("TELEGRAM_BOT_TOKEN")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

bot = Bot(token=Bot_Token)

# Bot utils import
from utils.command import CommandsMessages
from utils.buttons_functions import Buttons

buttons = Buttons(bot)


async def on_command(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    username = update.effective_user.username
    command = update.message.text

    command_message = CommandsMessages(bot)
    if command == '/start':
        await command_message.send_greeting_message(chat_id, username)
    elif command == '/help':
        await command_message.send_help_message(chat_id)
    elif command == '/courses':
        await command_message.send_courses_message(chat_id)
    else:
        await context.bot.send_message(
            chat_id=chat_id,
            text="Unknown command. Type /help for a list of available commands.",
            parse_mode="html"
        )


async def courses_button(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat.id
    username = query.from_user.username
    message = query.data
    if message == "hacking_courses":
        await bot.sendMessage(chat_id=chat_id, text="Hacking Courses", reply_markup=buttons.hacking_courses_button(),
                              parse_mode="html")
    elif message == "web_dev_courses":
        await bot.sendMessage(chat_id=chat_id, text="Web Development Courses",
                              reply_markup=buttons.web_development_courses_button(), parse_mode="html")


async def echo(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    username = update.effective_user.username
    message = update.message.text
    if len(message) > 6:
        try:
            send_message = gemini_ai_response(message)
            await bot.sendMessage(text=send_message, chat_id=chat_id, parse_mode="markdown",
                                  reply_markup=buttons.menu_button())
        except Exception as e:
            print(e)
            await bot.sendMessage(text="Please wait and try again Later!!!", chat_id=chat_id, parse_mode="markdown")
    else:
        await bot.sendMessage(text="<b>Give some more information so I assist you better!!!</b>", chat_id=chat_id,
                              reply_markup=buttons.menu_button(),
                              parse_mode="html")


def gemini_ai_response(message):
    try:
        model = genai.GenerativeModel('gemini-pro')
        training_data = """
        Your are Bashisht, your name is Bashisht, you are a large language model trained by TheCyberWorld. 
        You only have to answer the query which are related to the Information Technology, Cyber Security and Web Development.
        Answer should be precise and do not include the <b> tag in your response. 
        AND If the query is not related to these two topics just send the response: "Currently I have no information about it!!!"
        here is the query:
        """
        prompt_data = f"{training_data} {message}"
        response = model.generate_content(prompt_data, stream=True)
        response.resolve()
        # print(response.resolve())
        split_text = response.text
        # print(split_text)
    except Exception as e:
        print(e)
        split_text = "Please wait and try again!!!"
    return split_text


def to_markdown(text):
    text = text.replace('•', '  *')
    # print(text)
    split_text = text
    try:
        split_text = Markdown(textwrap.indent(text, prefix='', predicate=lambda _: True))
        # print(split_text)
    except Exception as e:
        print(e)
    return split_text.data


# run the bot
if __name__ == '__main__':
    application = ApplicationBuilder().token(Bot_Token).build()

    start_handler = CommandHandler(['start', 'help', 'courses'], on_command)
    application.add_handler(start_handler)

    button_handler = CallbackQueryHandler(courses_button)
    application.add_handler(button_handler)

    echo_handler = MessageHandler(filters.TEXT, echo)
    application.add_handler(echo_handler)

    application.run_polling()
    print("I am Here")
