try:
    from . import db_connection
except:
    import db_connection
import psycopg2
import json
import time

def get_self_challenge(user_id):
    conn=db_connection.get_connection()
    cursor=conn.cursor()
    result_dict={}
    try:
        SQL_QUERY="SELECT * FROM self_challenge WHERE id=%s"
        cursor.execute(SQL_QUERY,(user_id,))
        result=cursor.fetchall()
        res=[]
        try:
            for row in result:
                result_dict={
                    'c_id':row[0],
                    'id':row[1],
                    'descripition':row[2],
                    'imageurl':row[3],
                    'eventname':row[4],
                    'steps':row[5],
                    'calories':row[6]
                }
                res.append(result_dict)
        except IndexError as e:
            result_dict={'error':e}
    except (Exception,psycopg2.Error) as error:
        print(error)
        return error

    return res

