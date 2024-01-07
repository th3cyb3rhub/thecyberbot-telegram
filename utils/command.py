from utils.buttons_functions import Buttons
import os
from telegram import Bot
from dotenv import load_dotenv
load_dotenv()
Bot_Token = os.getenv("TELEGRAM_BOT_TOKEN")
bot = Bot(token=Bot_Token)
buttons = Buttons(bot)


class CommandsMessages:

    def __init__(self, bot):
        self.bot = bot

    async def send_greeting_message(self, chat_id, username):
        await self.bot.send_message(
            chat_id=chat_id,
            text=f"""
<b>आपको नमस्कार @{username}</b> ! 
हमारे टेलीग्राम बॉट में आपका स्वागत है।
हम आपके कौशल को बढ़ाने के लिए आपको मुफ्त ऑनलाइन पाठ्यक्रम प्रदान करने के लिए उत्साहित हैं।
हमारे संसाधनों का अन्वेषण करें और अपने ज्ञान को बढ़ावा दें!
""",
            reply_markup=buttons.menu_button(),
            parse_mode="html")

    async def send_help_message(self, chat_id):
        await self.bot.send_message(
            chat_id=chat_id,
            text=f"""
<b>Available commands:</b>

/start - Start the bot
/courses - Show available courses
""",
            parse_mode="html", reply_markup=buttons.menu_button())

    async def send_courses_message(self, chat_id):
        await self.bot.send_message(
            chat_id=chat_id,
            text=f"""
<b>Available courses:</b>
        """,
            reply_markup=buttons.menu_button(),
            parse_mode="html")
