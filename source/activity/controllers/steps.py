from flask import  Blueprint,jsonify
from flask_cors import CORS,cross_origin


from ..steps import check_is_present,add_step_activity,update_step_activity
from ..steps import get_step_count

steps_api =Blueprint('steps_api',__name__)

# Allow cors
CORS(steps_api)



@steps_api.route('/api/activity/steps/testConnection',methods=['GET','POST'])
def test_steps_connection():
    return jsonify({"connection":"hello world "})




@steps_api.route('/api/activity/steps/addToDatabase',methods=['GET','POST'])
def add_to_database():
    user_id,steps,date,info=('nikil@hotmail.com',124,'2018-02-18',{"ok":"test123"})
    status=''"Done"
    # create  a new entry if not present 
    if not check_is_present.check_step_entry(user_id,date):
        status="Is not in DB creating new entry"
        add_step_activity.add_to_database(user_id,steps,date,info)
    else:
        # If already present then create a Update the step count
        status="Is in DB updating step count"
        update_step_activity.update_step(user_id,steps,date)
    return jsonify({"status":status,"steps":steps})




@steps_api.route('/api/activity/steps/getSteps',methods=['GET','POST'])
def get_steps():
    user_id,date='nikil@gmail.com','2018-02-18'
    count=get_step_count.get_steps(user_id,date)[0]
    return jsonify({"stepcount":count,"user_id":user_id})