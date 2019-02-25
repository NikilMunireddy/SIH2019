try:
    from . import db_connection
except:
    import db_connection

import psycopg2
import json
import datetime

def get_gps_points(user_id,start_ts,end_ts):
    conn=db_connection.get_connection()
    cursor=conn.cursor()
    try:
        SQL_QUERY="SELECT * FROM gps_location WHERE time BETWEEN %s AND %s AND id=%s"
        value=(start_ts,end_ts,user_id)
        cursor.execute(SQL_QUERY,value)
        result=cursor.fetchall()
        if cursor.rowcount>0:
            status="success"
        else:
            status="No result"
    except (Exception ,psycopg2.Error)as error:
        print(error)
        status="Failed"

    result_dict={}
    try:
        for row in result:
            result_dict={
                'id':row[0],
                'gps_long':row[1],
                'gps_lat':row[2],
                'time':datetime.datetime.utcfromtimestamp(row[4]).strftime('%Y-%m-%dT%H:%M:%SZ')
            }
    except IndexError as e:
        result_dict={'error':e}
    res={
        'status':status,
        'data':result_dict
    }
    return res

if __name__ == "__main__":
    # yyyy/mm/dd
    import time_convert
    start_ts=time_convert.DMY_to_timestamp('2019-02-22')
    end_ts=time_convert.DMY_to_timestamp('2019-02-24')
    print(json.dumps(get_gps_points('1243',start_ts,end_ts),indent=2))