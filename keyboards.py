from aiogram import types


# Cпособы оплаты
def get_pay_method_keyboard(amount):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        types.InlineKeyboardButton("Cписать с баланса Личного кабинета", callback_data=f"balance_pay_sever_2:{amount}"),
        types.InlineKeyboardButton("Оплата онлайн", callback_data="online_pay"),
        types.InlineKeyboardButton("Отмена", callback_data="go_back")
    )
    return keyboard


# Получить ключ -> Amsterdam
def amsterdam_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    button = types.KeyboardButton('Назад')
    # создаем клавиатуру для выбора колличества месяцев подписки
    button1 = types.KeyboardButton('Amsterdam 1 месяц - 200 рублей')
    button2 = types.KeyboardButton('Amsterdam 2 месяца - 350 рублей')
    button3 = types.KeyboardButton('Amsterdam 3 месяца - 500 рублей')
    button6 = types.KeyboardButton('Amsterdam 6 месяцев - 900 рублей')

    keyboard.add(button1, button2, button3, button6, button)
    return keyboard


# Получить ключ -> Germany
def germany_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    button = types.KeyboardButton('Назад')
    # создаем клавиатуру для выбора колличества месяцев подписки
    button1 = types.KeyboardButton('Germany 1 месяц - 200 рублей')
    button2 = types.KeyboardButton('Germany 2 месяца - 350 рублей')
    button3 = types.KeyboardButton('Germany 3 месяца - 500 рублей')
    button6 = types.KeyboardButton('Germany 6 месяцев - 900 рублей')

    keyboard.add(button1, button2, button3, button6, button)
    return keyboard


# кнопка Баланс
def balance_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    button_balance = types.KeyboardButton('Пополнить баланс')
    button_auto = types.KeyboardButton('Включить автопродление')
    button = types.KeyboardButton('Назад')
    keyboard.add(button_balance, button_auto, button)

    return keyboard


# кнопка Назад
def back_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    button1 = types.KeyboardButton('Получить ключ')
    button2 = types.KeyboardButton('Мои ключи')
    button3 = types.KeyboardButton('Баланс')
    button4 = types.KeyboardButton('Заработать')
    keyboard.add(button1, button2, button3, button4)

    return keyboard


# Получить ключ
def get_keys():
    keyboard = types.ReplyKeyboardMarkup(row_width=1)
    button = types.KeyboardButton('Назад')
    button_Amsterdam = types.KeyboardButton('Amsterdam')
    button_Germany = types.KeyboardButton('Germany')
    keyboard.add(button_Germany, button_Amsterdam, button)

    return keyboard
