from flask import Blueprint,request,jsonify
from flask_cors import cross_origin,CORS
from ..UserPersonalInfo import add_user_info,get_user_info


user_personal_details=Blueprint('user_personal_details',__name__)

CORS(user_personal_details)

# POST REQUEST SINCE THE LENGTH OF THE QUERY URL IS LIMITED

'''--------ADD USER-------'''

@user_personal_details.route('/api/userPersonalDetails/adduser',methods=['GET','POST'])
def add_user_personal_details():
    user_id=request.args.get('id')
    fullname=request.args.get('fullname')
    first_name=request.args.get('first_name')
    last_name=request.args.get('last_name')
    photo_url=request.args.get('photo_url')
    misc=None   # A Json column
    status=add_user_info.add_to_database(user_id,fullname,first_name,last_name,photo_url,misc)
    return jsonify({'ret':status})


'''-------------GET USER INFO-------------'''

@user_personal_details.route('/api/userPersonalDetails/getUserInfo/<user_id>',methods=['GET','POST'])
def get_user_info_details(user_id):
    status,result=get_user_info.get_user_information(user_id)
    return jsonify({
            "status":status,
            'result':result
            })

