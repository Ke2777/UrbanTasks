from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text

API_TOKEN = '7360248683:AAElcUNNzBiDC-hv3rcsCjA7cH6y0zquQeY'

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(Text(equals="Calories", ignore_case=True))
async def set_age(message: Message):
    print("Команда 'Calories' получена.")
    await message.answer("Введите свой возраст:")
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message: Message, state: FSMContext):
    print("Получен возраст:", message.text)
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message: Message, state: FSMContext):
    print("Получен рост:", message.text)
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message: Message, state: FSMContext):
    print("Получен вес:", message.text)
    await state.update_data(weight=message.text)

    data = await state.get_data()
    age = int(data["age"])
    growth = int(data["growth"])
    weight = int(data["weight"])

    calories = 10 * weight + 6.25 * growth - 5 * age + 5
    await message.answer(f"Ваша норма калорий: {calories:.2f} ккал/день.")
    await state.finish()


if __name__ == '__main__':
    print("Bot is running...")
    executor.start_polling(dp, skip_updates=True)
