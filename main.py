# Third party imports

from flask import Flask
from flask_cors import CORS,cross_origin

app=Flask(__name__)

#-------------Local imports ----------------------
from source.activity.controllers.steps import steps_api
from source.activity.controllers.userCompetition import user_competition

#--------------------------------------------------


app.register_blueprint(steps_api)
app.register_blueprint(user_competition)

CORS(app)

if __name__ == "__main__":
    app.run(debug=True,port=8888)