try:
    from . import db_connection
except:
    import db_connection
    
import psycopg2
import json

def remove_user(user_id):
    try:
        conn=db_connection.get_connection()
        cursor=conn.cursor()
        SQL_QUERY="DELETE FROM user_personal_info WHERE id=%s"
        cursor.execute(SQL_QUERY,(user_id,))
        if cursor.rowcount>0:
            status="success"
        else:
            status="not-found"
    except(Exception, psycopg2.Error) as error:
        print(error)
        status="error"

    return status

if __name__ == "__main__":
    print(remove_user('1243'))