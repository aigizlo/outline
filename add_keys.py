import mysql.connector
from create_connection import create_connection
import datetime

from logger import logger


def add_keys(server_id, telegram_id, username, start_date, stop_date):
    mydb = create_connection()
    now = datetime.datetime.now()

    if mydb is None:
        logger.error('Не удалось создать соединение с БД', str(datetime.datetime.now()))
        return "Произошла ошибка, обратитесь к админстратору или попробуйте еще раз"

    try:
        with mydb.cursor(buffered=True) as mycursor:
            # узнаем user_id юзера
            mycursor.execute("SELECT user_id FROM users WHERE telegram_id = %s", ([telegram_id]))
            result_id = mycursor.fetchone()
            _userId = result_id[0]

            try:
                # обращаемся к бд, что бы взять несипользуемый ключ
                mycursor.execute("SELECT * FROM outline_keys WHERE used = %s AND server_id = %s", (0, server_id))
                result_id = mycursor.fetchone()
                _key_id, _outline_id, _sever_id, _key_value, _used = result_id
                logger.info(
                    f"Куплен неиспользуемы ключ id : {_key_id} для пользователя: {_userId}, время {now}")
            except Exception as e:
                logger.error(f'Ошибка при получении ключа из БД id пользователя: {_userId}, время : {now}, {e}')
                _key_value = "Произошла ошибка, обратитесь к админстратору"
                pass

            # меняем used c 0 на 1 у текущего ключа
            mycursor.execute("""UPDATE outline_keys SET used = 1 WHERE outline_key_id = %s AND used = 0""",
                             [_outline_id])

            # добавляем в таблицу user_keys приобретенный юзером ключ, + дата начала и конца действия ключа
            mycursor.execute(
                "INSERT INTO user_keys (user_id, key_id, name, start_date, stop_date) VALUES (%s, %s, %s, %s, %s)",
                (_userId, _key_id, username, start_date, stop_date)
            )

        return _key_value
    except mysql.connector.errors as err:
        logger.error(f'Произошла ошибка при добавлении ключа: {_userId}, время : {now}, {e}',
                     err)
        _key_value = "Произошла ошибка, обратитесь к админстратору"
    finally:
        return _key_value
