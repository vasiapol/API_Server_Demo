from flask_restful import reqparse
from db import mydb, mycursor
# Reads all arguments from the table
parser = reqparse.RequestParser()
mycursor.execute("SELECT * FROM TraineeList")
mycursor.fetchall()
for key in mycursor.description:
    print(key[0])
    parser.add_argument(key[0])
