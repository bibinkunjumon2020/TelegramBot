"""

This module Prompt the user to enter the city to fetch weather deatils,
define the function to get the weather information from OpenWeatherMap API,
parse the data and post accordingly.


Author: Bibin Kunjumon
Email: bibinkunjumon2020@gmail.com
Website:https://bibinkunjumon.me.uk/

"""

from telegram_bot import StatesGroup,State,Message,os,requests,logging,FSMContext,start_command


class WeatherStates(StatesGroup):
    GET_WEATHER_CITY = State()
# Prompt the user to enter the city to fetch weather deatils
async def weather_command(message: Message):
    await message.answer("Please enter the name of a city:")
    await WeatherStates.GET_WEATHER_CITY.set()


# Define the function to get the weather information from OpenWeatherMap API
async def get_weather_info(city_name: str) -> str:
    WEATHERAPI = os.getenv("API_WEATHER")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={WEATHERAPI}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the JSON response and format the weather information
        weather_data = response.json()
        weather_description = weather_data["weather"][0]["description"].capitalize()
        temperature = weather_data["main"]["temp"]
        feels_like = weather_data["main"]["feels_like"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        display_weather = f"The weather in {city_name} is {weather_description}.\n" \
                          f"The temperature is {temperature}°C, but it feels like {feels_like}°C.\n" \
                          f"The humidity is {humidity}% and the wind speed is {wind_speed} m/s."
        logging.info("Successfully Processed Weather Data\n" + display_weather)

        return display_weather
    else:
        logging.debug("Sorry, I couldn't get the weather information for this city. Please try again later.")
        return "Sorry, I couldn't get the weather information for this city. Please try again later."


# Define the function to handle the city name message
async def handle_city_name(message: Message, state: FSMContext):
    # Get the city name from the message text
    city_name = message.text
    # Get the weather information for the city
    weather_info = await get_weather_info(city_name)
    await message.answer(weather_info)
    await state.finish()
    # Pop up the command options 
    await start_command(message=message)