try:
    from . import db_connection
except:
    import db_connection

import psycopg2
import json
import time

def update_gps_coords(user_id,lang,lat,timestamp):
    conn=db_connection.get_connection()
    cursor=conn.cursor()
    status=None
    try:
        SQL_QUERY="UPDATE gps_location SET gps_long=%s , gps_lat=%s , time=%s WHERE id=%s"
        value=(str(lang).strip(),str(lat).strip(),timestamp,str(user_id).strip())
        cursor.execute(SQL_QUERY,value)
        conn.commit()
        if cursor.rowcount >0:
            status="success"
        else:
            status="Could Not insert"
        
    except (Exception,psycopg2.Error) as error:
        status="failed"
        print(error)
    return  status