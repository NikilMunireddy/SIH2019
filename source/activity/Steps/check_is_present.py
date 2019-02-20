try:
    from . import get_step_count
except:
    import get_step_count

def check_step_entry(user_id,date):
    count=get_step_count.get_steps(user_id,date)
    if len(count) >=1:
        # Entry is in the database 
        return True
    else:
        # Entry not in database
        return False
    

if __name__ == "__main__":
    print(check_step_entry('nikil@hotmail.com','2018-02-18'))
