try:
    from . import db_connection,check_is_present,update_steps
except:
    import db_connection,check_is_present,update_steps
import psycopg2
import json
import time

def add_step_count(user_id,steps,date,time,misc):
    try:
        conn=db_connection.get_connection()
        cursor=conn.cursor()
        SQL_QUERY="INSERT INTO steps (id, steps, date,time,misc) VALUES (%s,%s,%s,%s,%s)"
        record_insert=(user_id,steps,date,time,misc)
        if not check_is_present.is_present(user_id,date):
            cursor.execute(SQL_QUERY,record_insert)
            if cursor.rowcount >0:
                status="Success"
            else:
                status="Could Not insert"
        else:
            #update db
            print('in db')
            status=update_steps.update_user_steps(user_id,steps,date)
        conn.commit()

    except(Exception,psycopg2.Error) as error:
        status="failed"
        print(error)
        
    return status

if __name__ == "__main__":
    import time
    now =time.time()
    print(add_step_count('1243',1002,'2019-02-24',now,None))