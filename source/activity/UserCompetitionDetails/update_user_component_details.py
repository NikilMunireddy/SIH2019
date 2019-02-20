try:
    from . import db_conn,is_present
except:
    import db_conn,is_present
import psycopg2
import json

# NOTE Not Working

def update_table(fb_name,fb_id,no_of_comp,total_points,meta_dict):
    conn=db_conn.get_connection()
    curs=conn.cursor()

    SQL_QUERY="UPDATE user_competition_details SET no_of_comp=%s,total_points=%s WHERE fb_id=%s"
    values=(no_of_comp,total_points,fb_id)

    try:
        curs.execute(SQL_QUERY,values)
        comment =curs.rowcount+" Rows affeted"
        status=True
    except:
        comment="Could Not update the database"
        status=False
    return {"comment":comment,"status":status}
    
if __name__ == "__main__":
    fb_name='nikil'
    fb_id='nikilm@gmail.com'
    no_of_comp=41
    total_points=6
    meta_dict=json.dumps({'ok':123})
    print(json.dumps(update_table(fb_name,fb_id,no_of_comp,total_points,meta_dict),indent=2))