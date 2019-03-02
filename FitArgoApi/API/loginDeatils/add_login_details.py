try:
    from . import db_connection
except:
    import db_connection
import psycopg2
import json

def add_login_details(user_id,accsess_token,email_id,password,misc):
    conn=db_connection.get_connection()
    cursor=conn.cursor()
    try:
        SQL_QUERY="INSERT INTO login (id,access_tkn,email_id,password,misc) VALUES (%s,%s,%s,%s,%s)"
        value=(user_id,accsess_token,email_id,password,None)
        cursor.execute(SQL_QUERY,value)
        conn.commit()
        if cursor.rowcount > 0:
            status="success"
        else:
            status="could not insert"

    except (Exception, psycopg2.Error)  as error:
        print(error)
        status="failed"
    return status
