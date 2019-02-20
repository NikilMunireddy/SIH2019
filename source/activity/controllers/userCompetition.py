from flask import Blueprint,jsonify,request
from flask_cors import CORS,cross_origin
import json

#-----------Local imports-----------------
from ..UserCompetitionDetails import add_user_competition_details , get_user_competition_details
#---------------------------------------

user_competition=Blueprint('user_competition',__name__)


CORS(user_competition)

@user_competition.route('/api/activity/user_competition/testConnection',methods=['GET','POST'])
def test_user_competition_testConnection():
    return jsonify({"connection":"Test ok"})



@user_competition.route('/api/activity/user_competition/addCompetition',methods=['GET','POST'])
def add_user_competition():
    fb_name=request.args.get('fb_name')
    fb_id=request.args.get('fb_id')
    no_of_comp=request.args.get('no_of_comp')
    total_points=request.args.get('total_points')
    meta_dict=request.args.get('meta_dict')
    #status=add_user_competition_details.add_details(fb_name,fb_id,no_of_comp,total_points,meta_dict)
    print(fb_name,fb_id,no_of_comp,total_points,meta_dict)

    return jsonify({"status":"str(status)"})