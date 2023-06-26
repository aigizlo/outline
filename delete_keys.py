import datetime

from create_connection import create_connection

from config import apiurl_amsterdam, apicrt_amsterdam

from logger import logger

from outline_api import (

    Manager,
    get_key_numbers,
    get_active_keys)


mydb = create_connection()

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# cервер номер 1
manager_amsterdam = Manager(apiurl=apiurl_amsterdam, apicrt=apicrt_amsterdam)


def delete_keys(key_ids, ou_keys):
    now = datetime.datetime.now()
    # Удаление ключей из manager_amsterdam
    try:
        for id in ou_keys:
            if manager_amsterdam.delete(id):
                logger.info(f"ключ - {id} удален успешно")
    except Exception as e:
        logger.info(f"произошла ошбика при удалении ключей {ou_keys} из outline manager, {now} ", e)


    # Удаление ключей из базы данных user_keys
    placeholders = ", ".join(["%s"] * len(key_ids))
    cursor = mydb.cursor()
    query_user_keys = f"DELETE FROM user_keys WHERE key_id IN ({placeholders})"
    query_outline_keys = f"DELETE FROM outline_keys WHERE key_id IN ({placeholders})"

    try:
        cursor.execute(query_user_keys, key_ids)
        logger.info(f"Удаление ключей {key_ids}  из базы user_keys данных прошло успешно , {now} ")
    except Exception as e:
        logger.info(f"Не удалось удалить ключи {key_ids} в бд user_keys, " + str(datetime.datetime.now()), e)

    try:
        cursor.execute(query_outline_keys, key_ids)
        logger.info(f"Удаление ключей {key_ids} из базы outline_keys данных прошло успешно, время : {now} ")
    except Exception as e:
        print(f"Не удалось удалить ключи {key_ids} в бд outline_keys: {now} ", e)


