from flask_restful import Resource, abort
from db import mycursor, mydb
from args_parser import *
import Prometheus_client
# TraineeList
# shows a list of all trainees, and lets you POST to add new items


class TraineeList(Resource):
    REQUEST_TIME=Prometheus_client.Metrics.select_all_id
    @REQUEST_TIME.time()
    def get(self):
        mycursor.execute("SELECT * FROM TraineeList")
        result = mycursor.fetchall()
        if len(result) == 0:
            abort(404, Error="Table is empty")
        # JSONify output
        result = [dict(zip([key[0] for key in mycursor.description], row))
                  for row in result]
        return result, 200

    def post(self):
        args = parser.parse_args()
        sql = "INSERT INTO TraineeList (Firstname, Lastname ,Age) VALUES (%s, %s,%s)"
        val = (args['Firstname'], args['Lastname'], args['Age'])
        if all(arg is not None for arg in val):
            mycursor.execute(sql, val)
            mydb.commit()
        else:
            abort(400, Error="Some values of parameters are empty")
        return "Created", 201
