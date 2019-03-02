from flask import Blueprint,jsonify,request
from flask_cors import CORS,cross_origin
import time

from ..Registration import add_registration_details,get_registration_details
from ..loginDeatils import add_login_details
from ..UserPersonalInfo import add_user_info,get_user_info

user_registration=Blueprint('user_registration',__name__)

CORS(user_registration)



#--------insert registation details to adtabase--------'
# NOTE: Use 'POST' beacuse the data that can be encoded in URL is limited

# THIS PAGE ONLY 

@user_registration.route('/api/UserRegistration/registerUser/',methods=['GET','POST'])
def register_user():

    email_id=request.args.get("email")
    ## FB ID HERE
    user_id=email_id
    print("EMAIL",email_id)
    password=request.args.get('password')
    token=request.args.get("token")
    height=request.args.get('height')
    if height is None:
        height=150
    else:
        height=float(height)

    weight=request.args.get('weight')
    if weight is None:
        weight=60
    else:
        weight=float(weight)

    bmi=float(weight/(height/100)**2)
    # BMI = weight (kg)/height(m) ^2
    # name,token,
    misc=None
    status=add_user_info.add_to_database(user_id,email_id,"first_name","last_name","photo_url",None,email_id)
    status_reg=add_login_details.add_login_details("user_id","access_tkn",email_id,password,misc)

    status=add_registration_details.register_user_info(user_id,token,12,height,weight,bmi,misc)
    print(('status',status,'registration_status',status_reg))
    return jsonify({'status':status,'registration_status':status_reg})


# HTTP GET:
# Example: /api/UserRegistration/getRegisterdUser/1243
# returns the entire user details tuple
@user_registration.route('/api/UserRegistration/getRegisterdUser/<user_id>',methods=['GET','POST'])
def get_registerd_user(user_id):
    result=get_registration_details.get_registration_deatils(user_id)
    return jsonify({'result':result})