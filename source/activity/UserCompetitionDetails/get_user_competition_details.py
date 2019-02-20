try:
    from . import db_conn
except:
    import db_conn
import psycopg2
import json

def get_details(fb_id):
    conn=db_conn.get_connection()
    curs=conn.cursor()
 
    try:
        SQL_QUERY="SELECT * FROM user_competition_details WHERE fb_id=%s"

        curs.execute(SQL_QUERY,(fb_id,))
        conn.commit()
        result=curs.fetchall()[0]
        data={
            "fb_id":result[0],
            "fb_id":result[1],
            "no_of_comp":result[2],
            "total_points":result[3],
            "meta":result[4]
        }
        return data
        print(curs.rowcount)
    except(Exception ,psycopg2.Error) as Error:
        print(Error)


if __name__ == "__main__":
    print(json.dumps(get_details("nikilm@gmail.com"),indent=2))