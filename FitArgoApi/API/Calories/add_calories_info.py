try:
    from . import db_connection
except:
    import db_connection

import psycopg2
import json

def add_calories_information(user_id,date,calories_burnt,calories_consumed,misc):
    try:
        conn=db_connection.get_connection()
        cursor=conn.cursor()
        SQL_QUERY="INSERT INTO calories(id,date,calories_burnt,calories_consumed,misc) VALUES(%s,%s,%s,%s,%s)"
        value=(user_id,date,calories_burnt,calories_consumed,misc)

        cursor.execute(SQL_QUERY,value)
        conn.commit()
        if cursor.rowcount >0:
            status="Success"
        else:
            status="Could Not insert"
    except (Exception,psycopg2.Error) as error:
        print(error)
        status="failed"
    return status


if __name__ == "__main__":
    print(add_calories_information('1243','2019-02-23',1000,1300,None))