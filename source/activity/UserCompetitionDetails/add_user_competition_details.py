try:
    from . import db_conn,is_present
except:
    import db_conn,is_present
import psycopg2
import json


def add_details(fb_name,fb_id,no_of_comp,total_points,meta_dict):
    conn=db_conn.get_connection()
    curs=conn.cursor()
    status="Wait"
    SQL_QUERY="INSERT INTO user_competition_details (fb_name,fb_id,no_of_comp,total_points,meta) VALUES(%s,%s,%s,%s,%s)"
    values=(fb_name,fb_id,no_of_comp,total_points,meta_dict)
    try:
        if not is_present.is_present(fb_id):
            curs.execute(SQL_QUERY,values)
            conn.commit()
            status="Committed Successfully"
        else:
            status="Already exists in Database"

    except (Exception ,psycopg2.Error) as Error:
        print(Error)

    return status


if __name__ == "__main__":
    fb_name="nikil"
    fb_id="nikilm@gmail.com"
    no_of_comp=4
    total_points=6
    meta_dict=json.dumps({'ok':123})

    print(add_details(fb_name,fb_id,no_of_comp,total_points,meta_dict))
    
