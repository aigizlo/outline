import datetime

from add_keys import add_keys


# собираем данные и отправялем их в функицю add_keys для выбора неиспользываемого ключа
def generate_key(server_id, message, days):
    username = message.from_user.first_name
    telegram_id = message.from_user.id
    start_date = datetime.datetime.now()
    stop_date = start_date + datetime.timedelta(days=days)
    answer = add_keys(server_id, telegram_id, username, start_date, stop_date)
    return answer
