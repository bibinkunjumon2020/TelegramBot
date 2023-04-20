"""

This module pop up the greeting message and choice of commands
to proceed in bot functionailty.


Author: Bibin Kunjumon
Email: bibinkunjumon2020@gmail.com
Website:https://bibinkunjumon.me.uk/

"""

from telegram_bot import Message,logging

# Define the greeting message
async def start_command(message: Message):
    logging.info("Bot Operation Started")
    await message.answer("Hello! How can I assist you?\n"
                         "Please choose a function of the bot:\n"
                         "/weather - check weather in a city\n"
                         "/exchange - convert currencies\n"
                         "/animals - send a random cute animal picture\n"
                         "/poll - create a poll and send it to a group chat\n"
                          "/cancel - check weather in a city\n")

