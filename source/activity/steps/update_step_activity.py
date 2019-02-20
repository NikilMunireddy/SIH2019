try:
    from . import db_conn
except:
    import db_conn
import psycopg2

def update_step(user_id,steps,date):
    conn=db_conn.get_connection()
    curs=conn.cursor()

    SQL_QUERY="UPDATE user_steps SET steps = %s WHERE user_id = %s AND date= %s"
    values=(steps,user_id,date)
    try:
        curs.execute(SQL_QUERY,values)
        conn.commit()
        print(curs.rowcount, " record(s) affected")
        conn.close()
    except (Exception, psycopg2.Error)as error:
        print("Could not update database",error)

if __name__ == "__main__":
    print(update_step('nikil@hotmail.com',22,'2018-02-18'))