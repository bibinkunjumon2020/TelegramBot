"""

This module finishes the bot operation by finishing the state.


Author: Bibin Kunjumon
Email: bibinkunjumon2020@gmail.com
Website:https://bibinkunjumon.me.uk/

"""


from telegram_bot import types,FSMContext,logging


async def cancel_command(message: types.Message, state: FSMContext):
    """
    Handler for the /cancel command to cancel any ongoing operation.
    """
    await message.answer("Operation cancelled.")
    await state.finish()
    logging.info("Bot Operation Ended")
