import asyncio

from logger import logger

import datetime

from delete_keys import delete_keys

from create_connection import create_connection

from bot import send

sql_get_expired_keys = """
    SELECT u.telegram_id, uk.key_id, uk.name, ok.key_value, ok.outline_key_id, s.country     
    FROM user_keys uk     JOIN users u ON u.user_id = uk.user_id     
    JOIN outline_keys ok ON ok.key_id = uk.key_id     
    JOIN servers s ON s.server_id = ok.server_id     
    WHERE DATEDIFF(uk.stop_date, NOW()) = %s;
"""

mydb = create_connection()


# шаблоны для отправки сообщений
message_templates = {
    'KEY_EXPIRED': "{name}, срок вашего ключа '{key}', страна {country} истек, он был удален",
    'KEY_EXPIRES_IN_X_DAYS': "{name}, у вас осталось {days} до конца действия ключа '{key}', страна {country}",
}

# корректируем дни, дней, день
def plural_days(days):
    if 10 < days % 100 < 20:
        return f"{days} дней"
    else:
        rem = days % 10
        if rem == 1:
            return f"{days} день"
        elif 2 <= rem <= 4:
            return f"{days} дня"
        else:
            return f"{days} дней"

# ищем истекающие и истешие ключи и отправляем соответсвующее уведомление
def get_expired_keys_info():
    loop = asyncio.get_event_loop()
    cursor = mydb.cursor()
    now = datetime.datetime.now()

    # айди по которым будем удалять из outline manager
    id_for_delete_in_manager = []
    # айди по которым будем удалять из базы данных
    id_for_delet_in_bd = []

    for days in [5, 2, 0]:
        cursor.execute(sql_get_expired_keys, (days,))
        expired_keys = cursor.fetchall()

        try:
            for i in expired_keys:
                # распределяем данные по переменным
                id = i[0]
                key_id = i[1]
                name = i[2]
                key = i[3]
                ou_keys = i[4]
                country = i[5]

                # формируем тексты собщения
                text = message_templates['KEY_EXPIRES_IN_X_DAYS'].format(name=name,
                                                                         days=plural_days(days),
                                                                         key=key,
                                                                         country=country)
                if days == 0:
                    text = message_templates['KEY_EXPIRED'].format(name=name,
                                                                   days=days,
                                                                   key=key,
                                                                   country=country)
                    if ou_keys is not None:
                        id_for_delete_in_manager.append(ou_keys)
                    if key_id is not None:
                        id_for_delet_in_bd.append(key_id)
                    loop.run_until_complete(send(id, text))

                else:
                    # передаем данные id и текста для отправки сообщения пользователю
                    loop.run_until_complete(send(id, text))
        except Exception as e:
            logger.info(f"Ошибка при удалении ключей из баз данных ключей {id_for_delet_in_bd} и "
                        f"{id_for_delete_in_manager}, время {now} ", e)


    # передаем ключи для удаления
    if id_for_delet_in_bd and id_for_delete_in_manager:
        delete_keys(id_for_delet_in_bd, id_for_delete_in_manager)
