try:
    from . import db_conn
except:
    import db_conn
import psycopg2


def is_present(fb_id):
    conn=db_conn.get_connection()
    curs=conn.cursor()
    status=False
    try:
        SQL_QUERY="SELECT * from user_competition_details WHERE fb_id=%s"
        curs.execute(SQL_QUERY,(fb_id,))
        result=curs.fetchall()
        print("Length",len(result))
        if len(result)> 0:
            status= True
        else:
            status=False
        print(status)
    except (Exception ,psycopg2.Error) as Error:
        print(Error)
    return status

if __name__ == "__main__":
    fb_id="nikilm@gmail.com"
    is_present(fb_id)