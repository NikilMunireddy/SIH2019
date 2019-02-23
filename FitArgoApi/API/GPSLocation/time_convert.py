import time
import datetime

def DMY_to_timestamp(dmy):
    return time.mktime(datetime.datetime.strptime(dmy, "%Y-%m-%d").timetuple())

if __name__ == "__main__":
    print(DMY_to_timestamp('2011-12-01'))