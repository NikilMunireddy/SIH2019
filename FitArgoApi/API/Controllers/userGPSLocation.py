from flask import Blueprint,jsonify
from flask_cors import CORS,cross_origin
import time 
import datetime
from ..GPSLocation import add_gps_cord,get_gps_cord

user_gps_cords=Blueprint('user_gps_cords',__name__)
CORS(user_gps_cords)


@user_gps_cords.route('/api/GPSLocation/addCords/<user_id>/<long>/<lat>',methods=['GET','POST'])
def add_gps_cords(user_id,long,lat):
    ts=time.time()
    status=add_gps_cord.add_gps_cordianates(user_id,long,lat,ts)
    return jsonify({'status':status})


# yyyy/mm/dd  fomate 
@user_gps_cords.route('/api/GPSLocation/getCords/<user_id>/<start_date>/<end_date>',methods=['GET','POST'])
def get_cords(user_id,start_date,end_date):
    start_ts=time.mktime(datetime.datetime.strptime(start_date, "%Y-%m-%d").timetuple())
    end_ts=time.mktime(datetime.datetime.strptime(end_date, "%Y-%m-%d").timetuple())
    status,res=get_gps_cord.get_gps_points(user_id,start_ts,end_ts)
    return jsonify({"status":status,"result":res})