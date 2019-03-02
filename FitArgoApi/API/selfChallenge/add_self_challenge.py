try:
    from . import db_connection
except:
    import db_connection
import psycopg2
import json
import time

def add_self_challenge_details(c_id,user_id,descripition,imageurl,eventname,steps,calories):
    conn=db_connection.get_connection()
    cursor=conn.cursor()
    try:
        SQL_QUERY="INSERT INTO self_challenge (c_id,id,descripition,imageurl,eventname,steps,calories,misc) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        value=(c_id,user_id,descripition,imageurl,eventname,steps,calories,None)
        cursor.execute(SQL_QUERY,value)
        conn.commit()

        if cursor.rowcount > 0:
            status="success"
        else:
            status="could not insert"

    except (Exception,psycopg2.Error) as error:
        print(error)
        status="failed"

    return status
