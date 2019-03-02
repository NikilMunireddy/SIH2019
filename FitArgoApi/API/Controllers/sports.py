from flask import Blueprint,jsonify,request
from flask_cors import CORS,cross_origin

from ..Sports import addSportEvent,get_all_games,get_all_games_by_user_id

sports=Blueprint('sports',__name__)
CORS(sports)
#c_id,user_id,descripition,imageurl,eventname,steps,calories
# uid,location_lat,location_long,pdate,stime,etime,level,participants
@sports.route('/api/Sports/addEvent',methods=['GET','POST'])
def sports_method():
    uid=request.args.get('uid')
    location_lat=request.args.get('location_lat')
    location_long=request.args.get('location_long')
    pdate=request.args.get('pdate')
    stime=request.args.get('stime')
    etime=request.args.get('etime')
    level=request.args.get('level')
    participants=request.args.get('participants')

    status=addSportEvent.add_sport_event(uid,location_lat,location_long,pdate,stime,etime,level,participants)
    return jsonify({'status':status})


@sports.route('/api/Sports/getAllGames',methods=['GET','POST'])
def get_all_game_events():
    result=get_all_games.get_all_games()
    return jsonify({"result":result})

@sports.route('/api/Sports/getUserGames/',methods=['GET','POST'])
def get_add_user_games():
    user_id=request.args.get('id')
    result=get_all_games_by_user_id.get_all_games(user_id)
    return jsonify({"result":result})