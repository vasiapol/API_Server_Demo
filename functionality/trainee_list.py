from flask_restful import Resource, abort
from db import mycursor,mydb
from args_parser import *
# TraineeList
# shows a list of all trainees, and lets you POST to add new items


class TraineeList(Resource):
    def get(self):
        mycursor.execute("SELECT * FROM TraineeList")
        result = mycursor.fetchall()

        # JSONify output
        result = [dict(zip([key[0] for key in mycursor.description], row))
                  for row in result]
        return result

    def post(self):
        args = parser.parse_args()
        sql = "INSERT INTO TraineeList (Firstname, Lastname ,Age) VALUES (%s, %s,%s)"
        val = (args['Firstname'], args['Lastname'], args['Age'])
        if all(arg is not None for arg in val):
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
        else:
            abort(400, message="Wrong input some of parameters are empty")
        return "", 201
