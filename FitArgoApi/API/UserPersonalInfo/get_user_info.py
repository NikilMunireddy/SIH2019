try:
    from . import db_connection
except:
    import db_connection
    
import psycopg2
import json


def get_user_information(user_id):
    try:
        SQL_QUERY="SELECT * FROM user_personal_info WHERE id=%s"
        conn=db_connection.get_connection()
        cursor=conn.cursor()
        cursor.execute(SQL_QUERY,(user_id,))
        result=cursor.fetchall()
        print(result)
        if cursor.rowcount>0:
            status="Success"
        else:
            status="No result"

    except(Exception, psycopg2.Error) as error:
        print(error)
        status="Failed"

    return (status,result)


if __name__ == "__main__":
    get_user_information('1243')