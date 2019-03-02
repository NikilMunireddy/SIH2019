try:
    from . import db_connection
except:
    import db_connection

import psycopg2
import json

def authenticate_user(email_id,password):
    conn=db_connection.get_connection()
    cursor=conn.cursor()
    try:
        SQL_QUERY="SELECT access_tkn from login WHERE email_id=%s AND password=%s"
        value=(email_id,password)
        cursor.execute(SQL_QUERY,value)
        result=cursor.fetchall()
        if len(result) >=1:
            # Entry is in the database 
            status= True
        else:
            # Entry not in database
            status= False
    except(Exception ,psycopg2.Error) as error:
        print(error)
        status="failed"
    return status

 