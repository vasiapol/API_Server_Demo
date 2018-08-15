import mysql.connector
import json
import sys
# opens config file and loads json data
try:
    with open('db_conf.json') as f:
        json_data = json.load(f)
    mydb = mysql.connector.connect(
        host=json_data["db"]["host"],
        user=json_data["db"]["user"],
        passwd=json_data["db"]["passwd"],
        database=json_data["db"]["database"]
    )
except (EnvironmentError, ValueError):
    message="Error! Please check if configuration file exists and contains valid JSON data"
    sys.exit(message)
except (KeyError):
    message="Wrong configuration file"
    sys.exit(message)
except mysql.connector.errors.InterfaceError:
    message='Can not connect to MySQL server on {0}{1}'.format((json_data["db"]["host"]),":3306")
    #print(message)
    sys.exit(message)
else:
    mycursor = mydb.cursor()
    print("Successfully connected to the MySQL server...")
