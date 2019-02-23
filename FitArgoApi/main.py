from flask import Flask
from flask_cors import CORS,cross_origin

from API.Controllers.userPersonalInfo import user_personal_details
from API.Controllers.userRegistration import user_registration

app=Flask(__name__)

app.register_blueprint(user_personal_details)
app.register_blueprint(user_registration)

#--------------Run the flask Server ----------
if __name__ == "__main__":
    app.run(debug=True)
# deactivate the debug mode when in producttion mode
