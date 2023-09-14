from aiogram import types
from aiogram.dispatcher import FSMContext

from handlers.users.reg import is_authenticated
from keyboards.inline.brand_inline_button import main_menu_back, main_brand_inline_button
from loader import dp, db
from states.States import CommentState


@dp.callback_query_handler()
async def about_us(callback: types.CallbackQuery):
    if callback.data == "main_menu":
        photo_path = "image/brand_mebel.jpg"
        with open(photo_path, 'rb') as photo_file:
            await callback.message.answer_photo(photo=photo_file,
                                                reply_markup=main_brand_inline_button())

    elif callback.data == "about":
        photo_path = "image/brand_mebel.jpg"
        with open(photo_path, 'rb') as photo_file:
            await callback.message.answer_photo(photo=photo_file,
                                                caption="Lorem Ipsum is simply dummy text of the printing and typesetting "
                                                        "industry. Lorem Ipsum has been the industry's standard dummy text ever"
                                                        " since the 1500s, when an unknown printer took a galley of type and scrambled "
                                                        "it to make a type specimen book. It has survived not only five centuries, "
                                                        "but also the leap into electronic typesetting, remaining essentially unchanged.\n\n"
                                                        "🚚 Yetkazib berish bepul\n\n"
                                                        "📞+998919520505\n\n"
                                                        "@BrendMebel \n"
                                                        "@Brend_mebelqarshi",
                                                reply_markup=main_menu_back())
    elif callback.data == 'register':
        pass

    elif callback.data == "idea":
        user = is_authenticated(message=callback.message)
        if user == True:
            await callback.message.answer(text="<b>O'z fikrlaringizni yozib qodiring !\n</b>")
            await CommentState.comment.set()
        else:

            await callback.message.answer("You are not authenticated. Please authenticate to continue.", reply_markup=main_brand_inline_button())



@dp.message_handler(state=CommentState.comment)
async def comment(message: types.Message, state:FSMContext):
    db.add_comment(comment=message.text,
                   user_id=message.from_user.id
                   )
    await message.answer(text="Fikrlaringiz uchun rahmat ! ",
                         reply_markup=main_menu_back())
    await state.finish()
