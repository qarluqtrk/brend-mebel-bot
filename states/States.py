from aiogram.dispatcher.filters.state import StatesGroup, State


class Auth(StatesGroup):
    name = State()
    phone_number = State()
    location = State()


class OrderCustom(StatesGroup):
    type = State()
    size = State()

    # info branch