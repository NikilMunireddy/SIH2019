try:
    from . import db_connection,in_range
except:
    import db_connection,in_range

import psycopg2
import time
import json

def get_nearby_bois():
    conn=db_connection.get_connection()
    cursor=conn.cursor()
    try:
        SQL_QUERY="SELECT *  from gps_location ORDER BY time DESC"
        cursor.execute(SQL_QUERY)
        result=cursor.fetchall()
        long_lat=[]
        temp=[]
        in_x,in_y=result[0][1],result[0][2]
        for row in result:
            # TO ensure the same user is not included once again
            if in_x != row[1] and in_y!= row[2] and in_range.check_points_in_range(in_x,in_y,row[1],row[2],2000):
                temp.append(row[0])

                # long_lat.append(temp)

        return temp
            #SET GLOBAL FLAG TRUE

    except (Exception,psycopg2.Error) as error:
        print(error)
        raise Exception