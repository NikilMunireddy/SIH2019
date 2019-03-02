try:
    from . import db_connection
except:
    import db_connection

import psycopg2
import json



def register_user_info(id,name,age,height,weight,bmi,misc):
    conn=db_connection.get_connection()
    cursor=conn.cursor()
    status=""
    try:
        SQL_QUERY="INSERT INTO registration_detail(id,name,age,height,weight,bmi,misc) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        values=(id,name,age,height,weight,bmi,misc)
        cursor.execute(SQL_QUERY,values)
        conn.commit()
        if cursor.rowcount >0:
            status="success"
        else:
            status="Could Not insert"

    except(Exception, psycopg2.Error) as error:
        print(error)
        status="failed"
    
    return status


if __name__ == "__main__":
    print(register_user_info('1243','nik abc',21,173,68,26.1,None))