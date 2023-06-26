
from aiogram import types

from balance import pay_for_balance

from bot import dp, bot
from generate_key import generate_key
from keyboards import get_pay_method_keyboard

amount_to_days = {
    200: 1,
    350: 2,
    500: 3,
    900: 4
}


@dp.message_handler(lambda message: message.text == 'Amsterdam 1 месяц - 200 рублей')
async def process_back_command_am(message: types.Message):
    amount = 200
    submenu_keyboard = get_pay_method_keyboard(amount)

    answer = "Выберите способ оплаты:"

    await message.reply(answer, reply_markup=submenu_keyboard)


@dp.message_handler(lambda message: message.text == 'Amsterdam 2 месяца - 350 рублей')
async def process_back_command_am(message: types.Message):
    amount = 350
    submenu_keyboard = get_pay_method_keyboard(amount)

    answer = "Выберите способ оплаты:"

    await message.reply(answer, reply_markup=submenu_keyboard)


@dp.message_handler(lambda message: message.text == "Amsterdam 3 месяца - 500 рублей")
async def process_back_command_am(message: types.Message):
    amount = 500
    submenu_keyboard = get_pay_method_keyboard(amount)

    answer = "Выберите способ оплаты:"

    await message.reply(answer, reply_markup=submenu_keyboard)


@dp.message_handler(lambda message: message.text == "Amsterdam 6 месяцев - 900 рублей")
async def process_back_command_am(message: types.Message):
    amount = 900
    submenu_keyboard = get_pay_method_keyboard(amount)

    answer = "Выберите способ оплаты:"

    await message.reply(answer, reply_markup=submenu_keyboard)


@dp.callback_query_handler(lambda c: c.data.startswith("balance_pay_sever_1"))
async def process_balance_pay_callback_am(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    telegram_id = callback_query.from_user.id

    # Извлекаем сумму списания из callback_data
    _, amount_str = callback_query.data.split(":")
    amount = int(amount_str)

    days = amount_to_days.get(amount, None)

    server_id = 1

    generate_key(server_id, callback_query, days)

    answer = pay_for_balance(telegram_id, amount)

    main_menu_keyboard = types.InlineKeyboardMarkup(row_width=2)

    await bot.edit_message_text(answer, chat_id=callback_query.message.chat.id,
                                message_id=callback_query.message.message_id, reply_markup=main_menu_keyboard)