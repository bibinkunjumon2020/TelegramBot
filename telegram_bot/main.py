"""

This module starts the bot operation and Set up command handlers
& event handlers for different commands & chat states respectively.


Author: Bibin Kunjumon
Email: bibinkunjumon2020@gmail.com
Website:https://bibinkunjumon.me.uk/

"""

from telegram_bot import executor,logging, \
                        start_command,weather_command,exchange_command,animals_command,\
                        poll_command,cancel_command,handle_poll_question_options,\
                        handle_exchange_amount_currencies,handle_city_name,\
                        WeatherStates,ExchangeStates,PollStates,\
                        dispatcher



# Set up command handlers for different commands
dispatcher.register_message_handler(start_command, commands=["start"])
dispatcher.register_message_handler(weather_command, commands=["weather"])
dispatcher.register_message_handler(exchange_command, commands=["exchange"])
dispatcher.register_message_handler(animals_command, commands=["animals"])
dispatcher.register_message_handler(poll_command, commands=["poll"])
dispatcher.register_message_handler(cancel_command, commands=["cancel"])

# Set up event handlers for different chat states
dispatcher.register_message_handler(handle_city_name, state=WeatherStates.GET_WEATHER_CITY)
dispatcher.register_message_handler(handle_exchange_amount_currencies, state=ExchangeStates.GET_EXCHANGE_AMOUNT_CURRENCIES)
dispatcher.register_message_handler(handle_poll_question_options, state=PollStates.GET_POLL_QUESTION_OPTIONS)

if __name__ == "__main__":
    # Start the bot
    logging.info("Starting bot...")
    executor.start_polling(dispatcher, skip_updates=True)
