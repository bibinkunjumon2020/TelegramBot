"""

This module access a random picture of an animal from specified api
and post in bot chat area.


Author: Bibin Kunjumon
Email: bibinkunjumon2020@gmail.com
Website:https://bibinkunjumon.me.uk/

"""

from telegram_bot import types,aiohttp,logging,start_command

async def animals_command(message: types.Message):
    """
    Handler for the /animals command.
    """
    try:
        # Fetch a random picture of cute animals from an API such as thecatapi.com
        url = "https://api.thecatapi.com/v1/images/search"
        async with aiohttp.ClientSession() as session:  #this will avoid Unclosed connector & Unclosed client session Errors
            async with session.get(url) as response:
                response_json = await response.json()
        # Get the URL of the picture and send it to the user
        picture_url = response_json[0]["url"]
        await message.answer_photo(picture_url)
        logging.info("Successfully posted an Animal Pic")
        # Pop up the command options 
        await start_command(message=message)
    except:
        # Handle exceptions and errors
        await message.answer("Sorry, I couldn't fetch a picture of cute animals.")
        logging.debug("Couldn't fetch a picture of cute animals.")

