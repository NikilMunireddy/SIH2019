try:
    from . import db_conn,check_competition
except:
    import db_conn,check_competition
import psycopg2
import json


def add_competitiondetails(comp_id,comp_name,location_long,location_lat):
    conn=db_conn.get_connection()
    curs=conn.cursor()

    SQL_QUERY="INSERT INTO competition_details (comp_id,comp_name,location_long,location_lat) VALUES(%s,%s,%s,%s)"
    values=(comp_id,comp_name,location_long,location_lat)

    try:
        if not check_competition.is_present(comp_id):
            curs.execute(SQL_QUERY,values)
            conn.commit()
            print(curs.rowcount)
        else:
            print("Aready in DB")
    except(Exception ,psycopg2.Error) as Error:
        print(Error)


if __name__ == "__main__":
    comp_id="nikilm@hotmail.com"
    comp_name="running"
    location_long=72.11
    location_lat=12.11
    add_competitiondetails(comp_id,comp_name,location_long,location_lat)