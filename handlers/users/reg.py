from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default import reg_key
from keyboards.default.reg_key import cancel, loc
from loader import dp, db1
from states.States import RegistrationStates





def is_authenticated(message: types.Message) -> bool:
    # Retrieve the user's authentication status from the state (or database/storage)
    user = db1.get_user(id=message.from_user.id)
    if user:
        return True
    else:
        # User is not authenticated
        return False










@dp.message_handler(commands=['reg'])
async def start(message: types.Message):
    await message.reply("Welcome to the registration process! Please provide your phone number.", reply_markup=reg_key.phone_num())
    await RegistrationStates.waiting_for_phone_number.set()


@dp.message_handler(state=RegistrationStates.waiting_for_phone_number, content_types=types.ContentType.CONTACT)
async def process_phone_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_id'] = message['from']['id']
        data['phone_number'] = message['contact']['phone_number']
        data['full_name'] = f"{message['from']['first_name']} {message['from']['last_name']}"
        data['username'] = message['from']['username']

    # Ask for name
    await message.reply("Thank you! Please enter your name.", reply_markup=cancel())
    await RegistrationStates.waiting_for_name.set()


@dp.message_handler(state=RegistrationStates.waiting_for_name)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    # Ask for location
    await message.reply("Great! Now, please share your location.", reply_markup=loc())
    await RegistrationStates.waiting_for_location.set()


@dp.message_handler(content_types=types.ContentTypes.LOCATION, state=RegistrationStates.waiting_for_location)
async def process_location(message: types.Message, state: FSMContext):
    # Save location in state
    location = message.location
    async with state.proxy() as data:
        data['latitude'] = location.latitude
        data['longitude'] = location.longitude

    # Retrieve data from state
    db1.add_user(name=data['name'],
                phone_number=data['phone_number'],
                longitude=data['longitude'],
                latitude=data['latitude'])

    # Perform registration logic
    # ...

    # Reset state
    await state.finish()

    # Send confirmation message
    await message.reply("Thank you for registering! You're all set.")




# boldi ishladi
# boldi ishladi