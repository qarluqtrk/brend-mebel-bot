from aiogram.dispatcher.filters.state import StatesGroup, State


class RegistrationStates(StatesGroup):
    waiting_for_phone_number = State()
    waiting_for_name = State()
    waiting_for_location = State()

    # info branch