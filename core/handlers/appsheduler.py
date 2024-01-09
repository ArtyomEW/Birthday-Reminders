from datetime import datetime
from aiogram import Bot
import psycopg2


async def send_massage_to_week(bot: Bot):
    """Подключение к базе дынным"""

    database_connection_string = 'dbname=users user=postgres ' \
                                 'password=??????? host=127.0.0.1 port=5432'
    connection = psycopg2.connect(database_connection_string)
    cursor = connection.cursor()

    """Перебираем строки в столбце"""

    for i in range(1, 12):
        query = f"SELECT * FROM birth WHERE id = {i};"
        cursor.execute(query)
        data = cursor.fetchall()[0]
        date_for_if = datetime.now()
        date = str(datetime.now())
        year_today = f"{date[:-22]}-"
        name, date_of_birth, comment, data_for_send = data[1], data[2], data[3], year_today + data[4]
        if str(date_for_if.date()) == data_for_send:
            await bot.send_message(????????, f"Через неделю у {name} будет день рождение! Дата {date_of_birth[5:]}. "
                                               f"Комментарий: {comment}")
            return
    await bot.send_message(???????, 'Пока что нету дни рождения')
    cursor.close()
    connection.close()


async def send_message_to_day(bot: Bot):
    """Подключение к базе дынным"""

    database_connection_string = 'dbname=users user=postgres ' \
                                 'password=???????? host=127.0.0.1 port=5432'
    connection = psycopg2.connect(database_connection_string)
    cursor = connection.cursor()

    """Перебираем строки в столбце"""

    for i in range(1, 13):
        query = f"SELECT * FROM birth WHERE id = {i};"
        cursor.execute(query)
        data = cursor.fetchall()[0]
        date_for_if = datetime.now()
        date = str(datetime.now())
        year_today = f"{date[:-22]}-"
        name, date_of_birth, comment, data_for_send = data[1], data[2], data[3], year_today + data[5]
        if str(date_for_if.date()) == data_for_send:
            await bot.send_message(????????, f"Через один день у {name} будет день рождение! Дата {date_of_birth[5:]}. "
                                               f"Комментарий: {comment}")
            return
    await bot.send_message(????????, 'Пока что нету дни рождения')
    cursor.close()
    connection.close()
