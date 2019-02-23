from flask import Flask
from flask_cors import CORS,cross_origin

from API.Controllers.userPersonalInfo import user_personal_details
from API.Controllers.userRegistration import user_registration
from API.Controllers.userGPSLocation import user_gps_cords
from API.Controllers.userCalories import user_calories

app=Flask(__name__)

app.register_blueprint(user_personal_details)
app.register_blueprint(user_registration)
app.register_blueprint(user_gps_cords)
app.register_blueprint(user_calories)

#--------------Run the flask Server ----------
if __name__ == "__main__":
    app.run(debug=True)
# deactivate the debug mode when in producttion mode
