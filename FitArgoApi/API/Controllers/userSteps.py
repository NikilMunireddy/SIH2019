from flask import Blueprint,jsonify
from flask_cors import CORS,cross_origin
import time 
import datetime

from ..Steps import add_steps,get_step_details,get_steps_n_days

user_steps=Blueprint('user_steps',__name__)
CORS(user_steps)


# Insert steps into database, if entry already existess for the day then the database is updated
@user_steps.route('/api/userSteps/<user_id>/<steps>/<date>',methods=['GET','POST'])
def user_step_count(user_id,steps,date):
    ts=time.mktime(datetime.datetime.strptime(date, "%Y-%m-%d").timetuple())
    status=add_steps.add_step_count(user_id,steps,date,ts,None)
    return jsonify({'status':status})


# Returns steps of give day
@user_steps.route('/api/userSteps/<user_id>/<date>',methods=['GET','POST'])
def get_user_steps(user_id,date):
    steps=get_step_details.get_steps_info(user_id,date)
    return jsonify({"steps":steps})


# returns step count on 'n' days
@user_steps.route('/api/userSteps/<user_id>/<start>/<end>',methods=['GET','POST'])
def get_steps_of_n_days(user_id,start,end):
    start_ts=time.mktime(datetime.datetime.strptime(start, "%Y-%m-%d").timetuple())
    end_ts=time.mktime(datetime.datetime.strptime(end, "%Y-%m-%d").timetuple())
    n_days_steps=get_steps_n_days.get_steps_info(user_id,start_ts,end_ts)
    return jsonify({'steps':n_days_steps})
