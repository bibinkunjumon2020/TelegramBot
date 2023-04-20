"""

This module initialises the package 'telegram_bot' with import 
of necessary libraries and enviroment variables.Also list the 
modules need to be accessed across the package.


Author: Bibin Kunjumon
Email: bibinkunjumon2020@gmail.com
Website:https://bibinkunjumon.me.uk/

"""


import requests
import json
import aiohttp
from aiogram import Bot, Dispatcher, types,executor
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import logging
import os
from dotenv import load_dotenv
from pathlib import Path

# Set base directory and load environment variables
BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_path = os.path.join(BASE_DIR,".env")
load_dotenv(dotenv_path)
print(dotenv_path)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize the bot and set the API token
bot_token = os.getenv("API_BOT")
bot = Bot(token=bot_token, parse_mode=types.ParseMode.HTML)

# Initialize the dispatcher
dispatcher = Dispatcher(bot, storage=MemoryStorage())

# My Package module import
from .start import start_command
from .weather import weather_command,get_weather_info,handle_city_name,WeatherStates
from .exchange import exchange_command,handle_exchange_amount_currencies,ExchangeStates
from .poll import poll_command,handle_poll_question_options,PollStates
from .picture import animals_command
from .cancel import cancel_command

# Export module functions for external use
__all__=['start_command','weather_command','exchange_command','poll_command','animals_command',\
         'cancel_command','get_weather_info','handle_exchange_amount_currencies',\
         'handle_poll_question_options']