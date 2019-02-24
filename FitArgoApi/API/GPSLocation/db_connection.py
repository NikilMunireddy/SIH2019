import json
import psycopg2


# connects to the Postgres database and returns the connection object
def get_connection():
    with open(DB_CONFIG_FILE) as f:
        data = dict(json.load(f))
    try:
        conn = psycopg2.connect(**data)
        return conn
    except ConnectionAbortedError as error:
        print("Could not connect to database ")
        print(error)
        print("Exiting with satus code 1")
        exit(1)


def get_configuration():
    with open(DB_CONFIG_FILE) as f:
        data = dict(json.load(f))
    print(data)
    return data



if __name__ == "__main__":
    DB_CONFIG_FILE='../../dbconfig.json'
    get_connection()
else:
    DB_CONFIG_FILE="./dbconfig.json"
