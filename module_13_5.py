from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.files import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

API_TOKEN = ""
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

# Клавиатура
kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
kb.row(button1)
kb.row(button2)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text='Рассчитать')
async def set_age(message: types.Message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Пожалуйста, введите корректное числовое значение для возраста.')
        return
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Пожалуйста, введите корректное числовое значение для роста.')
        return
    await state.update_data(growth=int(message.text))
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Пожалуйста, введите корректное числовое значение для веса.')
        return
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    bmr = (10 * data['weight']) + (6.25 * data['growth']) - (5 * data['age']) + 5
    await message.answer(f'Ваша норма по количеству калорий в сутки: {bmr}')
    await state.finish()


@dp.message_handler()
async def all_messages(message: types.Message):
    """
    Обработчик для всех остальных сообщений.
    """
    await message.answer('Извините, я не понимаю это сообщение. Пожалуйста, выберите команду из меню или используйте кнопки.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
