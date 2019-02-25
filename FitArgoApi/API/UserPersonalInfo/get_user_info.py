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
                'fullname':row[1],
                'firstname':row[2],
                'lastname':row[3],
                'photourl':row[4]
            }
    except IndexError as e:
        result_dict={'error':e}
    res={
        'status':status,
        'data':result_dict
    }
    return res

if __name__ == "__main__":
    print(json.dumps(get_user_information('1243'),indent=2))