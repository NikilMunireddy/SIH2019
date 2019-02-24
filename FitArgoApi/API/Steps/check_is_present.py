try:
    from . import db_connection
except:
    import db_connection
import psycopg2
import json

def is_present(user_id,date):
    conn=db_connection.get_connection()
    cursor=conn.cursor()
    SQL_QUERY="SELECT steps FROM steps WHERE id= %s AND date= %s"
    value=(user_id,date)
    cursor.execute(SQL_QUERY,value)
    result=cursor.fetchall()
    if len(result) >=1:
        # Entry is in the database 
        return True
    else:
        # Entry not in database
        return False
 
 

if __name__ == "__main__":
    is_present('1243','2019-02-24')
