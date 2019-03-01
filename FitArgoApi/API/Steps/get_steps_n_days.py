try:
    from . import db_connection
except:
    import db_connection
import time
import datetime
import psycopg2
import json

'''
 Returns the list step count of "n" days, 
 example between 2019-03-01 and 2019-03-05 for a give user id
'''


def get_steps_info(user_id,date_start,date_end):
    conn=db_connection.get_connection()
    cursor=conn.cursor()
    try:
        SQL_QUERY="SELECT steps FROM steps WHERE time BETWEEN %s AND %s AND id=%s"
        value=(date_start,date_end,user_id)
        cursor.execute(SQL_QUERY,value)
        result=cursor.fetchall()
        if cursor.rowcount>0:
            status="success"
        else:
            status="No result"
    except(Exception, psycopg2.Error) as error:
        print(error)
        status="Failed"
    
    # convert to python dictonary
    result_dict={}
    try:
        for row in result:
            for count,day in enumerate(row):
                result_dict['day'+str(count)] = day
    except IndexError as e:
        result_dict={'error':e}

    res={
        "status":status,
        'data':result_dict
    }
    return res


if __name__ == "__main__":
    start_date='2019-02-22'
    end_date='2019-02-25'
    start_ts=time.mktime(datetime.datetime.strptime(start_date, "%Y-%m-%d").timetuple())
    end_ts=time.mktime(datetime.datetime.strptime(end_date, "%Y-%m-%d").timetuple())
    print(get_steps_info('1243',start_ts,end_ts))