from flask import Blueprint,jsonify,request
from flask_cors import CORS,cross_origin
from flask import abort
from ..Sports import addSportEvent,get_all_games,get_all_games_by_user_id

sports=Blueprint('sports',__name__)
CORS(sports)
#c_id,user_id,descripition,imageurl,eventname,steps,calories
# uid,location_lat,location_long,pdate,stime,etime,level,participants
@sports.route('/api/Sports/addEvent/',methods=['GET','POST'])
def sports_method():
    uid=request.args.get('uid')
    location_lat=None
    location_long=None
    pdate=request.args.get('pdate')
    stime=request.args.get('stime')
    etime=request.args.get('etime')
    level=request.args.get('level')
    participants=request.args.get('participants')
    address=request.args.get('address')
    gname=request.args.get('gname')
    try :   
        status=addSportEvent.add_sport_event(uid,location_lat,location_long,pdate,stime,etime,level,participants,address,gname)
        return jsonify({'status':status})
    except:
        abort(404)


@sports.route('/api/Sports/getAllGames/',methods=['GET','POST'])
def get_all_game_events():
    try:
        result=get_all_games.get_all_games()
        return jsonify({"result":result})

    except:
        return abort(404) 


@sports.route('/api/Sports/getUserGames/',methods=['GET','POST'])
def get_add_user_games():
    try:
        user_id=request.args.get('id')
        result=get_all_games_by_user_id.get_all_games(user_id)
        return jsonify({"result":result})
    except:
        return abort(404)   