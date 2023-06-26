from aiogram import types

from keyboards import get_pay_method_keyboard

from balance import pay_for_balance

from bot import dp, bot
from generate_key import generate_key

amount_to_days = {
    200: 1,
    350: 2,
    500: 3,
    900: 4
}


@dp.message_handler(lambda message: message.text == 'Germany 1 месяц - 200 рублей')
async def process_back_command_ger(message: types.Message):
    amount = 200
    submenu_keyboard = get_pay_method_keyboard(amount)

    answer = "Выберите способ оплаты:"

    await message.reply(answer, reply_markup=submenu_keyboard)


@dp.message_handler(lambda message: message.text == 'Germany 2 месяца - 350 рублей')
async def process_back_command_ger(message: types.Message):
    amount = 350
    submenu_keyboard = get_pay_method_keyboard(amount)

    answer = "Выберите способ оплаты:"

    await message.reply(answer, reply_markup=submenu_keyboard)


@dp.message_handler(lambda message: message.text == "Germany 3 месяца - 500 рублей")
async def process_back_command_ger(message: types.Message):
    amount = 500
    submenu_keyboard = get_pay_method_keyboard(amount)

    answer = "Выберите способ оплаты:"

    await message.reply(answer, reply_markup=submenu_keyboard)



@dp.message_handler(lambda message: message.text == "Germany 6 месяцев - 900 рублей")
async def process_back_command_ger(message: types.Message):
    amount = 900
    submenu_keyboard = get_pay_method_keyboard(amount)

    answer = "Выберите способ оплаты:"

    await message.reply(answer, reply_markup=submenu_keyboard)


@dp.callback_query_handler(lambda c: c.data.startswith("balance_pay_sever_2"))
async def process_balance_pay_callback_ger(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    telegram_id = callback_query.from_user.id

    # Извлекаем сумму списания из callback_data
    _, amount_str = callback_query.data.split(":")

    # cумма оплаты
    amount = int(amount_str)

    # колличетсво дней подписки
    days = amount_to_days.get(amount, None)

    # айди сервера, к которому покупался ключ доступа
    server_id = 2


    generate_key(server_id, callback_query, days)

    answer = pay_for_balance(telegram_id, amount)

    main_menu_keyboard = types.InlineKeyboardMarkup(row_width=2)
    await bot.edit_message_text(answer, chat_id=callback_query.message.chat.id,
                                message_id=callback_query.message.message_id, reply_markup=main_menu_keyboard)



@dp.callback_query_handler(lambda c: c.data == "go_back")
async def process_callback_go_back(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    main_menu_keyboard = types.InlineKeyboardMarkup(row_width=2)
    await bot.edit_message_text("Выберите действие:", chat_id=callback_query.message.chat.id,
                                message_id=callback_query.message.message_id, reply_markup=main_menu_keyboard)