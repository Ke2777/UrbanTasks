from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.files import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import initiate_db, fill_products, get_all_products
import sqlite3

API_TOKEN = ""
health_bot = Bot(token=API_TOKEN)
dispatcher = Dispatcher(health_bot, storage=MemoryStorage())

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
inline_menu = InlineKeyboardMarkup()

calorie_calc_button = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calculate_calories")
formulas_button = InlineKeyboardButton(text="Формулы расчёта", callback_data="show_formulas")

inline_menu.add(calorie_calc_button)
inline_menu.add(formulas_button)

calculate_button = KeyboardButton(text="Рассчитать")
info_button = KeyboardButton(text="Информация")
buy_button = KeyboardButton(text="Купить")

main_menu.add(calculate_button)
main_menu.add(info_button)
main_menu.add(buy_button)

inline_menu_products = InlineKeyboardMarkup()
for i in range(1, 5):
    inline_menu_products.add(InlineKeyboardButton(text=f'Product{i}', callback_data="product_buying"))


class UserInput(StatesGroup):
    age_state = State()
    height_state = State()
    weight_state = State()


@dispatcher.message_handler(commands=["start"])
async def start_conversation(message: types.Message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью.", reply_markup=main_menu)


@dispatcher.message_handler(text="Рассчитать")
async def show_options(message: types.Message):
    await message.answer("Выберите опцию:", reply_markup=inline_menu)


@dispatcher.callback_query_handler(text="show_formulas")
async def display_formulas(callback_query: types.CallbackQuery):
    await callback_query.message.answer("10 x вес + 6.25 х рост - 5 * возраст + 5")
    await callback_query.answer()


@dispatcher.callback_query_handler(text="calculate_calories")
async def request_age(callback_query: types.CallbackQuery):
    await callback_query.message.answer("Введите свой возраст:")
    await UserInput.age_state.set()


@dispatcher.message_handler(state=UserInput.age_state)
async def request_height(message: types.Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    await message.answer("Введите свой рост:")
    await UserInput.height_state.set()


@dispatcher.message_handler(state=UserInput.height_state)
async def request_weight(message: types.Message, state: FSMContext):
    await state.update_data(height=int(message.text))
    await message.answer("Введите свой вес:")
    await UserInput.weight_state.set()


@dispatcher.message_handler(state=UserInput.weight_state)
async def calculate_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=int(message.text))
    user_data = await state.get_data()
    calorie_norm = (10 * user_data["weight"]) + (6.25 * user_data["height"]) - (5 * user_data["age"]) + 5
    await message.answer(f"Ваша норма по количеству калорий в сутки: {calorie_norm}")
    await state.finish()


@dispatcher.message_handler(text='Купить')
async def get_buying_list(message: types.Message):
    products = get_all_products()
    for product in products:
        await message.answer_photo(
            photo="https://via.placeholder.com/150",
            caption=f'Название: {product[1]} | {product[2]} | Цена: {product[3]}'
        )

    await message.answer("Выберите продукт для покупки:", reply_markup=inline_menu_products)


@dispatcher.callback_query_handler(text="product_buying")
async def send_confirm_message(callback_query: types.CallbackQuery):
    await callback_query.message.answer("Вы успешно приобрели продукт!")
    await callback_query.answer()


@dispatcher.message_handler()
async def all_messages(message: types.Message):
    await message.answer(
        "Извините, я не понял вашего запроса. Пожалуйста, используйте меню для взаимодействия со мной.",
        reply_markup=main_menu)


if __name__ == "__main__":
    initiate_db()
    fill_products()
    executor.start_polling(dispatcher, skip_updates=True)
