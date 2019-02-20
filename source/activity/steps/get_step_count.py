try:
    from . import db_conn
except:
    import db_conn


def get_steps(user_id,date):
    conn=db_conn.get_connection()
    curs=conn.cursor()

    SQL_QUERY="SELECT steps FROM user_steps WHERE user_id= %s AND date= %s"
    values=(user_id,date)
    curs.execute(SQL_QUERY,values)
    result=curs.fetchall()
    conn.commit()
    conn.close()

    return result


if __name__ == "__main__":
    print(get_steps('nikil@hotmail.com','2018-02-18'))