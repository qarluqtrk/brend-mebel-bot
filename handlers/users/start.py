from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.brand_inline_button import main_brand_inline_button
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    photo_path = "image/brand_mebel.jpg"
    with open(photo_path, 'rb') as photo_file:
        await message.answer_photo(photo=photo_file,
                                   reply_markup=main_brand_inline_button())