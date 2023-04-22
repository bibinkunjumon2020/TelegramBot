"""

This module Prompt the user to enter the question and answer options
in a specified format and post the poll in chat room specified 
by specific id.


Author: Bibin Kunjumon
Email: bibinkunjumon2020@gmail.com
Website:https://bibinkunjumon.me.uk/

"""

from telegram_bot import StatesGroup,State,types,FSMContext,logging,bot,start_command



class PollStates(StatesGroup):
    GET_POLL_QUESTION_OPTIONS = State()

async def poll_command(message: types.Message):
    """
    Handler for the /poll command.
    """
    # Prompt the user to enter the question and answer options
    await message.answer("Please enter the question you want to ask and the answer options separated by commas, "
                          "for example: 'What is your favorite color?, Red, Blue, Green'")
    # Set the state to GET_POLL_QUESTION_OPTIONS
    await PollStates.GET_POLL_QUESTION_OPTIONS.set()


async def handle_poll_question_options(message: types.Message, state: FSMContext):
    """
    Handler for getting the question and answer options from the user for the poll command.
    """
    # Split the question and answer options entered by the user
    input_text = message.text.split(",")

    if len(input_text) >= 2:
        question = input_text[0]  # First index is Question
        options = input_text[1:]  # All other values are options
        logging.info(f"Poll Input Question & Options  {question},{options}")
        try:
            chat_id = message.chat.id # if you hae a group id,give that poll will post in that
            logging.info(f"Poll Posting chat-id ,{chat_id}")
            await bot.send_poll(chat_id, question=question,options=options)
            logging.info("Successfully Created Poll")
        except Exception as e :
                logging.debug(f"Error in Sending poll,{e}")
                await message.answer("Sorry, I couldn't  send the poll.")
        finally:
            await state.finish()
            # Pop up the command options 
            await start_command(message=message)
    else:
        # Handle incorrect input
        await message.answer("Incorrect input. Please enter the question and answer options separated by commas, "
                              "for example: 'What is your favorite color?, Red, Blue, Green'")
        logging.debug("Poll Format Wrong")
       

