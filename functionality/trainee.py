import re
from flask_restful import Resource, abort, reqparse
from db import mydb, mycursor, id_exist
from args_parser import *

# Trainee
# shows a single trainee item and lets you delete a trainee item


class Trainee(Resource):
    def get(self, trainee_id):
        # Check if exists
        if id_exist(trainee_id):

            sql = 'SELECT * FROM TraineeList WHERE ID= {0}'.format(trainee_id)
            mycursor.execute(sql)
            result = mycursor.fetchall()
            mydb.commit()
            # JSONify output
            result = [dict(zip([key[0] for key in mycursor.description], row))
                      for row in result]
        else:
            abort(404, message="Trainee with the specified ID {} doesn't exist".format(
                trainee_id))
        return result, 200

    def delete(self, trainee_id):
        if id_exist(trainee_id):
            sql = '{0} {1}'.format(
                "DELETE FROM TraineeList WHERE ID =", trainee_id)
            mycursor.execute(sql)
            mydb.commit()
        else:
            abort(404, message="Trainee with the specified ID {} doesn't exist".format(
                trainee_id))
        return '{0}'.format("1 record deleted"), 200

    def patch(self, trainee_id):
        args = parser.parse_args()
        # update only if arg value is not null

        for param in args:
            if args[param] is not None:
                sql = 'UPDATE TraineeList SET {0} = "'"{1}"'" WHERE ID={2}'.format(
                    param, args[param], trainee_id)
                mycursor.execute(sql)
                mydb.commit()
        return "1 record affected", 201
