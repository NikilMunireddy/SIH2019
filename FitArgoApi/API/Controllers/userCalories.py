from flask import Blueprint,jsonify
from flask_cors import CORS,cross_origin

from ..Calories import add_calories_info,get_calories_info

user_calories=Blueprint('user_calories',__name__)
CORS(user_calories)

@user_calories.route('/api/Calories/addCalories/<user_id>/<date>/<burnt>/<consumed>',methods=['GET','POST'])
def add_user_information(user_id,date,burnt,consumed):
    status=add_calories_info.add_calories_information(user_id,date,burnt,consumed,None)
    return jsonify({"status":status})


@user_calories.route('/api/Calories/getCaloriesInfo/<user_id>/<date>',methods=['GET','POST'])
def get_calories_information(user_id,date):
    result=get_calories_info.get_calories_info(user_id,date)
    return jsonify({"result":result})