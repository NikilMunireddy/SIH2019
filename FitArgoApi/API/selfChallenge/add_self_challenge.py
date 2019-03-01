try:
    from . import db_connection
except:
    import db_connection
import psycopg2
import json
import time

def add_self_challenge_details(c_id,user_id,imageurl,eventname,steps,calories):
    pass