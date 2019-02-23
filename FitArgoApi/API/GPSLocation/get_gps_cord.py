try:
    from . import db_connection
except:
    import db_connection

import psycopg2
import json


def get_gps_points(user_id,start_ts,end_ts):
    conn=db_connection.get_connection()
    cursor=conn.cursor()
    try:
        SQL_QUERY="SELECT * FROM gps_location WHERE time BETWEEN %s AND %s AND id=%s"
        value=(start_ts,end_ts,user_id)
        cursor.execute(SQL_QUERY,value)
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

if __name__ == "__main__":
    # yyyy/mm/dd
    import time_convert
    start_ts=time_convert.DMY_to_timestamp('2019-02-22')
    end_ts=time_convert.DMY_to_timestamp('2019-02-24')
    get_gps_points('1243',start_ts,end_ts)