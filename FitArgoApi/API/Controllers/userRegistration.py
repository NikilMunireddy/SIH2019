from flask import Blueprint,jsonify,request
from flask_cors import CORS,cross_origin

from ..Registration import add_registration_details,get_registration_details

user_registration=Blueprint('user_registration',__name__)

CORS(user_registration)

#POST Request

'''--------insert registation details to adtabase--------'''
@user_registration.route('/api/UserRegistration/registerUser',methods=['GET','POST'])
def register_user():
    user_id=request.args.get('id')
    name=request.args.get('name')
    age=int(request.args.get('age'))
    height=float(request.args.get('height'))
    weight=float(request.args.get('weight'))
    bmi=float(request.args.get('bmi'))
    misc=None

    status=add_registration_details.register_user_info(user_id,name,age,height,weight,bmi,misc)
    return jsonify({'Status':status})


@user_registration.route('/api/UserRegistration/getRegisterdUser/<user_id>',methods=['GET','POST'])
def get_registerd_user(user_id):
    status,result=get_registration_details.get_registration_deatils(user_id)
    return jsonify({"status":status,'result':result})