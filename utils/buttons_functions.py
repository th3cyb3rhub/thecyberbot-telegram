from telegram import InlineKeyboardButton, InlineKeyboardMarkup


class Buttons:
    def __init__(self, bot):
        self.bot = bot


    def menu_button(self):  # Corrected indentation and added `self`
        keyboard = [
            [InlineKeyboardButton("Hacking Courses", callback_data="hacking_courses")],
            [
                InlineKeyboardButton("Web Development Courses", callback_data="web_dev_courses"),
                InlineKeyboardButton("See all Courses and Roadmaps", url="https://www.thecyberhub.org/roadmaps")
            ]
        ]
        return InlineKeyboardMarkup(keyboard)


    def hacking_courses_button(self):  # Corrected indentation and added `self`
        keyboard = [
            [InlineKeyboardButton("Cyber Security Beginner",
                                  url="https://www.thecyberhub.org/roadmaps/cyber-security-beginner")],
            [
                InlineKeyboardButton("Bug Hunting", url="https://www.thecyberhub.org/roadmaps/bug-hunting"),
                InlineKeyboardButton("Penetration and Vulnerability Tester",
                                     url="https://www.thecyberhub.org/roadmaps/penetration-and-vulnerability-tester")
            ]
        ]
        return InlineKeyboardMarkup(keyboard)


    def web_development_courses_button(self):  # Corrected indentation and added `self`
        keyboard = [
            [InlineKeyboardButton("Mern Stack Developer",
                                  url="https://www.thecyberhub.org/roadmaps/mern-stack-roadmap")],
            [
                InlineKeyboardButton("React Native Developer",
                                     url="https://www.thecyberhub.org/roadmaps/next-js-roadmap"),
                InlineKeyboardButton("Next JS Developer",
                                     url="https://www.thecyberhub.org/roadmaps/react-native-roadmap")
            ]
        ]
        return InlineKeyboardMarkup(keyboard)
