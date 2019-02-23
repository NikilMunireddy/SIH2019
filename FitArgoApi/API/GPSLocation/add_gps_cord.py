try:
    from . import db_connection
except:
    import db_connection

import psycopg2
import json
import time


def add_gps_cordianates(user_id,long,lat,timestamp):
    conn=db_connection.get_connection()
    cursor=conn.cursor()

    try:
        SQL_QUERY="INSERT INTO gps_location(id,gps_long,gps_lat,time) VALUES(%s,%s,%s,%s)"
        value=(user_id,long,lat,timestamp)
        print(type(timestamp))
        cursor.execute(SQL_QUERY,value)
        conn.commit()
        if cursor.rowcount >0:
            status="Success"
        else:
            status="Could Not insert"
    except(Exception,psycopg2.Error) as error:
        print(error)
    return status

if __name__ == "__main__":
    timestamp=time.time()
    add_gps_cordianates('1243',12.973,70.63663,timestamp)