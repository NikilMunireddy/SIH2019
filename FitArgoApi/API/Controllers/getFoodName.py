from flask import Blueprint,jsonify,request
from flask_cors import CORS,cross_origin

import os

food_name=Blueprint('food_name',__name__)
CORS(food_name)

# POST Request
@food_name.route('/api/foodName',methods=['GET','POST'])
def get_food_name():
    if 'photo' in request.files:
        file = request.files['photo']
        print(file.filename)
        file.save('./API/Images/'+file.filename)
        # get the name of the food , the image is stored in "./API/Images" folder 
        result,calories="idly",600
        print(result,calories)
        return jsonify({
            'success' : True,
            'prediction' : result,
            'calories':calories
            })
    else:
        return jsonify({'success':False})
