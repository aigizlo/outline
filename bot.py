from aiogram import Bot, Dispatcher
from config import token


bot = Bot(token=token)

dp = Dispatcher(bot)


async def send_message(chat_id, text):
    await bot.send_message(chat_id=chat_id, text=text)

# Пример использования функции
async def send(chat_id, message_text):

    await send_message(chat_id, message_text)