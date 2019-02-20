from flask import Blueprint,jsonify
from flask_cors import CORS,cross_origin

#-----------Local imports-----------------

#---------------------------------------

user_competition=Blueprint('user_competition',__name__)


CORS(user_competition)

@user_competition.route('/api/activity/user_competition/testConnection',methods=['GET','POST'])
def test_user_competition_testConnection():
    return jsonify({"connection":"user_competition"})