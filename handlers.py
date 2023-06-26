from create_connection import create_connection
from key_list import get_user_keys
from bot import dp
from balance import balance
from keyboards import *

mydb = create_connection()


@dp.message_handler(lambda message: message.text == 'Мои ключи')
async def process_get_key_command(message: types.Message):
    # создаем клавиатуру с кнопкой "Назад"
    keyboard = types.ReplyKeyboardMarkup(row_width=1)
    button = types.KeyboardButton('Назад')
    keyboard.add(button)
    telegram_id = message.from_user.id
    answer = get_user_keys(telegram_id)
    await message.reply(answer, reply_markup=keyboard)


# обрабатываем нажатие кнопки "Получить ключ"
@dp.message_handler(lambda message: message.text == 'Получить ключ')
async def process_get_key_command(message: types.Message):
    # импортируем кливатуру
    keyboard = get_keys()
    answer = "Выберите страну:"

    await message.reply(answer, reply_markup=keyboard)


# обрабатываем нажатие кнопки "Amsterdam"
@dp.message_handler(lambda message: message.text == 'Amsterdam')
async def process_back_command(message: types.Message):
    # импортируем кливатуру
    keyboard = amsterdam_keyboard()
    # отправляем сообщение с текстом "Главное меню" и клавиатурой с четырьмя кнопками
    await message.reply("Выберите, на сколько месяцев оформить подписку", reply_markup=keyboard)



# обрабатываем нажатие кнопки "Germany"
@dp.message_handler(lambda message: message.text == 'Germany')
async def process_back_command(message: types.Message):

    keyboard = germany_keyboard()

    # отправляем сообщение с текстом "Главное меню" и клавиатурой с четырьмя кнопками
    await message.reply("Выберите, на сколько месяцев оформить подписку", reply_markup=keyboard)


# обрабатываем нажатие кнопки "Заработать"
@dp.message_handler(lambda message: message.text == 'Заработать')
async def process_back_command(message: types.Message):
    # создаем клавиатуру с кнопкой "Назад"
    keyboard = types.ReplyKeyboardMarkup(row_width=1)
    button = types.KeyboardButton('Назад')
    keyboard.add(button)

    answer2 = "Здесь будет введена система промокодов"

    # отправляем сообщение с текстом "Главное меню" и клавиатурой с четырьмя кнопками
    await message.reply(answer2, reply_markup=keyboard)


# обрабатываем нажатие кнопки "Баланс"
@dp.message_handler(lambda message: message.text == 'Баланс')
async def process_back_command(message: types.Message):
    # создаем клавиатуру с кнопкой "Назад"
    keyboard = balance_keyboard()

    user_balance = balance(message.from_user.id)

    answer2 = f"Ваш баланс {user_balance} рублей"

    # отправляем сообщение с текстом "Главное меню" и клавиатурой с четырьмя кнопками
    await message.reply(answer2, reply_markup=keyboard)


# обрабатываем нажатие кнопки "Назад"
@dp.message_handler(lambda message: message.text == 'Назад')
async def process_back_command(message: types.Message):
    # создаем клавиатуру с четырьмя кнопками
    keyboard = back_keyboard()

    # отправляем сообщение с текстом "Главное меню" и клавиатурой с четырьмя кнопками
    await message.reply("Главное меню", reply_markup=keyboard)
