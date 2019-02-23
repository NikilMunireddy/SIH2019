try:
    from . import db_connection
except:
    import db_connection

import psycopg2
import json

def get_gps_points(user_id):
    conn=db_connection.get_connection()
    cursor=conn.cursor()

    try:
        SQL_QUERY="SELECT * FROM gps_location WHERE id=%s"
        cursor.execute(SQL_QUERY,(user_id,))
        result=cursor.fetchall()
        print(result)
        if cursor.rowcount>0:
            status="Success"
        else:
            status="No result"
    except (Exception ,psycopg2.Error)as error:
        print(error)
        status="Failed"
    return (status,result)

