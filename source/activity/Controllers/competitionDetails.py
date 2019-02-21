from flask import Blueprint,jsonify
from flask_cors import CORS,cross_origin

competition_details=Blueprint('competition_details',__name__)


@competition_details.route('/api/activity/CompetitionDetails/testConnection')
def competition_details_test():
    return jsonify({"Connection":"Ok"})