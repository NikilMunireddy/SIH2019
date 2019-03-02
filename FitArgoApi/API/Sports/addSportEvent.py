try:
    from . import db_connection
except:
    import db_connection
import psycopg2
import json
import time

#NOTE games 

def add_sport_event(uid,location_lat,location_long,pdate,stime,etime,level,participants):
    conn=db_connection.get_connection()
    print(uid,location_lat,location_long,pdate,stime,etime,level,participants)
    cursor=conn.cursor()
    try:
        SQL_QUERY="INSERT INTO games (uid,location_lat,location_long,pdate,stime,etime,level,participants) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        value=(uid,location_lat,location_long,pdate,stime,etime,level,participants)
        cursor.execute(SQL_QUERY,value)
        if cursor.rowcount > 0:
            status="success"
        else:
            status="could not insert"
    except (Exception,psycopg2.Error) as error:
        print(error)
        status='failed'
    return status