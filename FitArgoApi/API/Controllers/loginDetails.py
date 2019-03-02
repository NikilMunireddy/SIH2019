from flask import Blueprint,jsonify,request
from flask_cors import CORS,cross_origin

from API.loginDeatils import add_login_details
from API.loginDeatils import auth_user

login_details=Blueprint("login_details",__name__)

@login_details.route("/api/loginDetails/addCreds/",methods=['GET','POST'])
def add_login_creds():
    email_id=request.args.get("email_id")
    password=request.args.get("password")
    misc=None
    status=add_login_details.add_login_details("user_id","access_tkn",email_id,password,misc)
    return jsonify({'status':status})


@login_details.route('/api/loginDetails/getAuth/<email_id>/<password>',methods=['GET','POST'])
def get_auth(email_id,password):
    status=auth_user.authenticate_user(email_id,password)
    return jsonify({"status":status})