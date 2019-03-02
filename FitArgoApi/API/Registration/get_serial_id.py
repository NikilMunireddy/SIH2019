try:
    from . import db_connection
except:
    import db_connection

import psycopg2
import json

def get_serial_id(user_id):
    conn=db_connection.get_connection()
    cursor=conn.cursor()
    try:
        SQL_QUERY="SELECT sid FROM registration_detail WHERE id=%s"
        cursor.execute(SQL_QUERY,(user_id,))
        result=cursor.fetchall()
        
        return result[0][0]
    except (Exception,psycopg2.Error) as identifier:
        print(identifier)

if __name__ == "__main__":
    print(get_serial_id('52501'))