try:
    from . import db_connection
except:
    import db_connection
import psycopg2
import json

def is_present(user_id):
    conn=db_connection.get_connection()
    cursor=conn.cursor()
    SQL_QUERY="SELECT id FROM gps_location WHERE id=%s "
    cursor.execute(SQL_QUERY,(user_id,))
    result=cursor.fetchall()
    if len(result) >=1:
        return True
    else:
        return False

