"""

This module Create a new state group for handling currency exchange,
Prompt the user to enter the amount and currencies to convert,
Fetch the exchange rate from an API such as Exchange Rates API.


Author: Bibin Kunjumon
Email: bibinkunjumon2020@gmail.com
Website:https://bibinkunjumon.me.uk/

"""

from telegram_bot import StatesGroup,State,types,FSMContext,logging,os,requests,json


# Create a new state group for handling currency exchange
class ExchangeStates(StatesGroup):
    GET_EXCHANGE_AMOUNT_CURRENCIES = State()

async def exchange_command(message: types.Message, state: FSMContext):
    """
    Handler for the /exchange command.
    """
    # Prompt the user to enter the amount and currencies to convert
    await message.answer("Please enter the amount you want to convert and the currencies separated by spaces, "
                         "for example: '10 USD EUR'")
    # Set the state to GET_EXCHANGE_AMOUNT_CURRENCIES
    await ExchangeStates.GET_EXCHANGE_AMOUNT_CURRENCIES.set()


async def handle_exchange_amount_currencies(message: types.Message, state: FSMContext):
    """
    Handler for getting the amount and currencies from the user for the exchange command.
    """
    # Extract the amount and currencies entered by the user
    input_text = message.text.split()
    if len(input_text) == 3:
        amount = input_text[0]
        from_currency = input_text[1]
        to_currency = input_text[2]
        logging.info(f"Converting from {from_currency} to {to_currency}")

        try:

            url = f"https://api.apilayer.com/fixer/convert?to={to_currency}&from={from_currency}&amount={amount}"
            payload = {}
            headers = {
                "apikey": os.getenv("API_EXCHANGE")  # Fetch the exchange rate from an API such as Exchange Rates API
            }
            response = requests.request("GET", url, headers=headers, data=payload)
            status_code = response.status_code
            result = response.text
            json_data = f'{result}'
            try:
                data = json.loads(json_data)
            except Exception as e:
                logging.debug("error", e)
            success = data["success"]
            query = data["query"]
            from_currency = query["from"]
            to_currency = query["to"]
            amount = query["amount"]
            date_exchange = data["date"]
            exchanged_amount = data["result"]
            logging.info(
                f"Status : {success},\nDate of Exchange : {date_exchange},\n{amount} {from_currency} = {exchanged_amount} {to_currency}")
            await message.answer(
                f"Date of Exchange : {date_exchange}\n{amount} {from_currency} = {exchanged_amount} {to_currency}")
        except:
            # Handle exceptions and errors
            logging.info("Couldn't convert the currencies.")
            await message.answer("Sorry, I couldn't convert the currencies.")

        finally:
            # Reset the state
            await state.finish()
    else:
        # Handle incorrect input
        logging.debug("Incorrect input")
        await message.answer("Incorrect input. Please enter the amount and currencies separated by spaces, "
                             "for example: '10 USD EUR'.")
