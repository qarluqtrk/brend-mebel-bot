from aiogram.dispatcher.filters.state import StatesGroup, State


class AuthState(StatesGroup):
    name = State()
    phone_number = State()
    location = State()


class OrderCustomState(StatesGroup):
    type = State()
    size = State()


class CommentState(StatesGroup):
    comment = State()

