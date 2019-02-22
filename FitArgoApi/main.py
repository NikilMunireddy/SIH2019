from flask import Flask
from flask_cors import CORS,cross_origin


app=Flask(__name__)


#--------------Run the flask Server ----------
app.run(debug=True)
# deactivate the debug mode when in producttion mode
