import psycopg2
from datetime import datetime, timedelta

person = 1


def read_and_insert_data(file_path, database_connection_string):

    connection = psycopg2.connect(database_connection_string)
    cursor = connection.cursor()

    try:
        # Открываем файл и читаем данные
        with open(file_path, 'r', encoding='UTF-8') as file:
            lines = file.readlines()

        global person

        for line in lines:
            data = line.strip().split(', ')
            name, birth_date, comment = data

            notification = str(datetime.strptime(birth_date, '%Y.%m.%d') - timedelta(days=7))[0:-9]
            one_day_is_notice = str(datetime.strptime(notification, '%Y-%m-%d') + timedelta(days=6))[5:-9]

            sql_query = f"INSERT INTO birth (id, name, birth_date, comment, notification, one_day_is_notice) " \
                        f"VALUES ('{person}', '{name}', '{birth_date}','{comment}', " \
                        f"'{str(notification)[5:]}', '{one_day_is_notice}') "
            person += 1
            cursor.execute(sql_query)

            connection.commit()
    except Exception as e:
        print(f"Нету никакой ошибки: {e}")

        connection.rollback()

    finally:
        cursor.close()
        connection.close()


file_path = 'peoples.txt'

database_connection_string = 'dbname=users user=postgres password=aarrttyyoomm host=127.0.0.1 port=5432'

read_and_insert_data(file_path, database_connection_string)
