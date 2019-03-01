try:
    from . import db_connection
except:
    import db_connection

import psycopg2
import json

def add_to_database(user_id,username,first_name,last_name,photo_url,misc,email):
    conn=db_connection.get_connection()
    cursor=conn.cursor()
    status=""
    try:
        SQL_QUERY="INSERT INTO user_personal_info(id,username,first_name,last_name,photo_url,misc,email) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        values=(user_id,username,first_name,last_name,photo_url,misc,email)
        cursor.execute(SQL_QUERY,values)
        conn.commit()
        status="Success"
    except(Exception,psycopg2.Error) as error:
        print(error)
        status="failed"

    return status

if __name__ == "__main__":
    add_to_database('1243','nik abc','nik','abc','https://google.com',None,"nikil@gmail.com")
