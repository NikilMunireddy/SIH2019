try:
    from . import db_connection
except:
    import db_connection
import psycopg2
import json
import time

#NOTE games 

def add_sport_event(uid,location_lat,location_long,pdate,stime,etime,level,participants,address,gname):
    conn=db_connection.get_connection()
    print(uid,location_lat,location_long,pdate,stime,etime,level,participants,address)
    cursor=conn.cursor()
    try:
        SQL_QUERY="INSERT INTO games (uid,location_lat,location_long,pdate,stime,etime,level,participants,address,gname) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        value=(uid,location_lat,location_long,pdate,stime,etime,level,participants,str(address),gname)
        cursor.execute(SQL_QUERY,value)
        conn.commit()
        if cursor.rowcount > 0:
            status="success"
        else:
            raise Exception
        conn.close()
    except (Exception,psycopg2.Error) as error:
        print(error)
        raise Exception
    return status