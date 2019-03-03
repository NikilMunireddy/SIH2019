from flask import Blueprint,jsonify,request
from flask_cors import CORS,cross_origin
from flask import abort
from ..GPSLocation import add_gps_cord
from ..GPSLocation import in_range,check_is_present,update_coords,get_near_by_bois
from .. import flags
import time


geo_cord=Blueprint('geo_cord',__name__)
CORS(geo_cord)

@geo_cord.route('/api/GPSLocation/update/',methods=['GET','POST'])
def add_cords_to_db():
    user_id=request.args.get('id')
    longitude=request.args.get('lang')
    latitude=request.args.get('lat')
    timestamp=time.time()
    status=None
    try:
        if not check_is_present.is_present(user_id):
            status=add_gps_cord.add_gps_cordianates(user_id,str(longitude),str(latitude),timestamp)
        else:
            status=update_coords.update_gps_coords(user_id,str(longitude),str(latitude),timestamp)
        if not flags.challenge_running:
              users=get_near_by_bois.get_nearby_bois() 
              if(len(users)>2):
                    flags.challenge_running=True
                    users.remove(user_id)
                    flags.users=users
        else:
            if(len(users)>0):
                if(user_id in flags.users):
                    flags.users.remove(user_id)
                    return jsonify({'status':status,"action":"notify"})             
        return jsonify({'status':status,"action":"nill"})
    except:
        abort(404)    
@geo_cord.route('/api/GPSLocation/getNearBy/',methods=['GET','POST'])
def get_near_by_people():
    pass
