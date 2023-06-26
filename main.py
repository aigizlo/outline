from aiogram.utils import executor
from bot import dp
from expider_keys import get_expired_keys_info

from handlers import process_get_key_command

from handlers_amsterdam import process_back_command_am

from handlers_germany import process_back_command_ger

import datetime

from create_connection import create_connection

import asyncio
from aiogram import types


from logger import logger

mydb = create_connection()

subscription_periods = {
    'Amsterdam 1 месяц - 200 рублей': 31,
    'Amsterdam 2 месяца - 350 рублей': 62,
    "Amsterdam 3 месяца - 500 рублей": 92,
    "Amsterdam 6 месяцев - 900 рублей": 182,
    "Germany 1 месяц - 200 рублей": 31,
    "Germany 2 месяца - 350 рублей": 62,
    "Germany 3 месяца - 500 рублей": 92,
    "Germany 6 месяцев - 900 рублей'": 182
}


# обрабатываем команду /start
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    mycursor = mydb.cursor()

    # создаем клавиатуру с четырьмя кнопками
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    button1 = types.KeyboardButton('Получить ключ')
    button2 = types.KeyboardButton('Мои ключи')
    button4 = types.KeyboardButton('Заработать')
    keyboard.add(button1, button2, button4)

    username = message.from_user.first_name
    telegram_id = message.from_user.id
    # проверем, есть ли данный юзер в таблице users
    mycursor.execute("SELECT * FROM users WHERE telegram_id = %s", (telegram_id,))
    result = mycursor.fetchone()

    if result is None:
        mycursor.execute(
            "INSERT INTO users (username, telegram_id) VALUES (%s, %s)",
            (username, telegram_id)
        )
        # отправляем приветственное сообщение и клавиатуру пользователю
    await message.reply("Добрый день, уважаемый пользователь!", reply_markup=keyboard)
    logger.debug('Обработка команды /start')


process_back_command_am
process_get_key_command
process_back_command_ger

if __name__ == '__main__':
    # запускаем бота
    loop = asyncio.get_event_loop()
    get_expired_keys_info()
    executor.start_polling(dp, skip_updates=False)
    logger.info('Бот запущен ' + str(datetime.datetime.now()))