import json
import psycopg2

CONFIG_FILE_PATH='./dbconfig.json'


# Connects to the database and returns the connection object 
def get_connection():
    with open(CONFIG_FILE_PATH) as f:
        data = dict(json.load(f))
    try:
        conn = psycopg2.connect(**data)
        return conn
    except ConnectionAbortedError:
        print("Could not connect to database ")
        print("Exiting with satus code 1")
        exit(1)

if __name__ == "__main__":
    get_connection()
