try:
    from . import db_conn
except:
    import db_conn
import psycopg2
import json

def add_to_database(user_id,steps,date,info):
    try:
        conn=db_conn.get_connection()
        curs=conn.cursor()

        SQL_QUERY="INSERT INTO user_steps (user_id, steps, date,info) VALUES (%s,%s,%s,%s)"
        record_insert=(user_id,steps,date,json.dumps(info))

        curs.execute(SQL_QUERY,record_insert)
        conn.commit()
        print(curs.rowcount)
    except(Exception, psycopg2.Error)as error:
        print(error)


if __name__ == "__main__":
    user_id="nikil@hotmail.com"
    steps=122
    date="2018-02-18"
    info={"info":"ok"}
    add_to_database(user_id,steps,date,info)