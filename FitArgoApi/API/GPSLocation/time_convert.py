import time
import datetime

def DMY_to_timestamp(dmy):
    return time.mktime(datetime.datetime.strptime(dmy, "%d/%m/%Y").timetuple())

if __name__ == "__main__":
    print(DMY_to_timestamp('01/12/2011'))