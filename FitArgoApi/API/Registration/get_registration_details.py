try:
    from . import db_connection
except:
    import db_connection

import psycopg2
import json

def get_registration_deatils(user_id):
    conn=db_connection.get_connection()
    cursor=conn.cursor()
    try:
        SQL_QUERY="SELECT * FROM registration_detail WHERE id=%s"
        cursor.execute(SQL_QUERY,(user_id,))
        result=cursor.fetchall()
        if cursor.rowcount>0:
            status="success"
        else:
            status="No result"
    except(Exception, psycopg2.Error) as error:
        print(error)
        status="Failed"
    result_dict={}

    try:
        for row in result:
            result_dict={
                'id':row[0],
                'name':row[1],
                'age':row[2],
                'height':row[3],
                'weight':row[4],
                'bmi':row[5]
            }
    except Exception as identifier:
        print(identifier)
    res={
        "status":status,
        'data':result_dict
    }
    return res

if __name__ == "__main__":
    print(json.dumps(get_registration_deatils('1243'),indent=2))
