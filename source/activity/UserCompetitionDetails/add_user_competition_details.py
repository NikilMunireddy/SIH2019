try:
    from . import db_conn
except:
    import db_conn
import psycopg2
import json

def add_details(fb_name,fb_id,no_of_comp,total_points,meta):
    conn=db_conn.get_connection()
    curs=conn.cursor()

    try:
        SQL_QUERY="INSERT INTO user_competition_details(fb_name,fb_id,no_of_comp,total_points,meta) VALUES (%s,%s,%s,%s,%s)"
        values=(fb_name,fb_id,no_of_comp,total_points,meta)
        
        curs.execute(SQL_QUERY,values)
        conn.commit()
        print(curs.rowcount)
    except(Exception ,psycopg2.Error) as Error:
        print(Error)


if __name__ == "__main__":
    fb_name="nikil"
    fb_id="nikilm@gmail.com"
    no_of_comp=4
    total_points=6
    meta_dict={"ok":"123"}
    meta=json.dumps(meta_dict)
    add_details(fb_name,fb_id,no_of_comp,total_points,meta)