try:
    from . import db_conn
except:
    import db_conn
import psycopg2
import json

def is_present(comp_id):
    conn=db_conn.get_connection()
    curs=conn.cursor()
    status=False
    try:
        SQL_QUERY="SELECT * from competition_details WHERE comp_id=%s"
        curs.execute(SQL_QUERY,(comp_id,))
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
    id="nikilm@gmail.com"
    is_present(id)