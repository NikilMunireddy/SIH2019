try:
    from . import db_connection
except:
    import db_connection
    
import psycopg2
import json

def get_steps_info(user_id,date):
    try:
        SQL_QUERY="SELECT steps FROM steps WHERE id=%s AND date=%s"
        value=(user_id,date)
        conn=db_connection.get_connection()
        cursor=conn.cursor()
        cursor.execute(SQL_QUERY,value)
        result=cursor.fetchall()
        if cursor.rowcount>0:
            status="Success"
        else:
            status="No result"
    except(Exception, psycopg2.Error) as error:
        print(error)
        status="Failed"

    return (status,result)


if __name__ == "__main__":
    print(get_steps_info('1243','2019-02-24'))