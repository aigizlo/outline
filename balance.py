from create_connection import create_connection

from logger import logger

import datetime

from generate_key import generate_key


mydb = create_connection()

cursor = mydb.cursor()

qsl_current_balance = """SELECT SUM(user_balance_ops.amount)
                FROM user_balance_ops
                JOIN users ON user_balance_ops.user_id = users.user_id
                WHERE users.telegram_id = %s"""

sql_pay_query = """INSERT INTO user_balance_ops (user_id, opdate, amount) 
                SELECT user_id, 
                CURRENT_TIMESTAMP, - %s FROM users WHERE telegram_id = %s """


# делаем запрос в бд и смотрим  баланс пользователя
def balance(telegram_id):
    cursor.execute(qsl_current_balance, (telegram_id,))
    cur_balance = cursor.fetchone()[0]
    if cur_balance is None:
        cur_balance = 0
    return cur_balance


# покупка с баланса личного кабинета
def pay_for_balance(telegram_id, amount):
    current_balance = balance(telegram_id)

    try:
        if current_balance >= amount:
            now = datetime.datetime.now()
            cursor.execute(sql_pay_query, (amount, telegram_id))

            answer = """Покупка прошла успешно, перейдите в раздел "Мои ключи " для получения ключа доступа. """

            logger.info(f"Покупка на сумму {amount} прошла успешно, время покупки : {now}, пользователь - {telegram_id}")
        else:
            answer = "Недостаточно средств"

        return answer

    except Exception as e:
        logger.info(f" Произошла ошбика при покупке на сумму - {amount},  у пользователя {telegram_id}, его баланс {current_balance}, время {now}", e)

        answer = "Произошла ошибка, обратитесь к админстратору"

    finally:
        return answer

