from flask import Blueprint,jsonify,request
from flask_cors import CORS,cross_origin

from ..Registration import add_registration_details,get_registration_details

user_registration=Blueprint('user_registration',__name__)

CORS(user_registration)



#--------insert registation details to adtabase--------'
# NOTE: Use 'POST' beacuse the data that can be encoded in URL is limited

@user_registration.route('/api/UserRegistration/registerUser',methods=['GET','POST'])
def register_user():
    user_id=request.args.get('id')
    name=request.args.get('name')
    age=int(request.args.get('age'))
    height=float(request.args.get('height'))
    weight=float(request.args.get('weight'))
    bmi=float(request.args.get('bmi'))
    # BMI = weight (kg)/height(m) ^2
    misc=None

    status=add_registration_details.register_user_info(user_id,name,age,height,weight,bmi,misc)
    return jsonify({'Status':status})


# HTTP GET:
# Example: /api/UserRegistration/getRegisterdUser/1243
# returns the entire user details tuple
@user_registration.route('/api/UserRegistration/getRegisterdUser/<user_id>',methods=['GET','POST'])
def get_registerd_user(user_id):
    result=get_registration_details.get_registration_deatils(user_id)
    return jsonify({'result':result})