from flask_restful import Resource, abort
from db import mycursor, mydb
from args_parser import *
# TraineeList
# shows a list of all trainees, and lets you POST to add new items


class TraineeList(Resource):
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
        arg_count="%s,"*len(args)
        arg_count=arg_count[:-1]
        sql = "INSERT INTO TraineeList () VALUES ({})".format(arg_count)
        val = [0,]
        for value in args.itervalues():
            if value is not None:
                val.append(value)
        if len(val)==len(args):
            mycursor.execute(sql, val)
            mydb.commit()
        else:
            abort(400, Error="Some values of parameters are empty")
        return "Created", 201
