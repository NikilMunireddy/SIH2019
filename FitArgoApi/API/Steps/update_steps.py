try:
    from . import db_connection
except:
    import db_connection
import psycopg2
import json

def update_user_steps(user_id,steps,date):
    conn=db_connection.get_connection()
    cursor=conn.cursor()
    try:
        SQL_QUERY="UPDATE steps SET steps = %s WHERE id = %s AND date= %s"
        value=(steps,user_id,date)
        cursor.execute(SQL_QUERY,value)
        conn.commit()
        if cursor.rowcount >0:
            status="Success"
        else:
            status="Could Not insert"
    except (Exception ,psycopg2.Error) as Error:
        print(Error)
        status='failed'
    return status

if __name__ == "__main__":
    print(update_user_steps('1243',2000,'2019-02-24'))
