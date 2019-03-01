try:
    from . import db_connection
except:
    import db_connection

import psycopg2
import json


def get_calories_info(user_id, date):
    conn = db_connection.get_connection()
    cursor = conn.cursor()
    try:
        SQL_QUERY = "SELECT * FROM calories WHERE id=%s AND date=%s"
        value = (user_id, date)
        cursor.execute(SQL_QUERY, value)
        result = cursor.fetchall()

        if cursor.rowcount > 0:
            status = "success"
        else:
            status = "No result"
    except (Exception, psycopg2.Error)as error:
        print(error)
        status = "Failed"
    result_dict = {}

    try:
        for row in result:
            result_dict = {
                'id': row[0],
                'date': str(row[1]),
                'calories_burnt': row[2],
                'calories_consumed': row[3]
            }
    except IndexError as e:
        result_dict={'error':e}
    res = {
        'status': status,
        'data': result_dict
    }
    return res


if __name__ == "__main__":
    print(json.dumps(get_calories_info('1243', '2019-02-23'), indent=2))
