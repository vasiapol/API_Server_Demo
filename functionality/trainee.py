import re
from flask_restful import Resource, abort,reqparse
from db import mycursor,mydb
from args_parser import *

# Trainee
# shows a single trainee item and lets you delete a trainee item


class Trainee(Resource):
    def get(self, trainee_id):
        sql = 'SELECT * FROM TraineeList WHERE ID= {0}'.format(trainee_id)
        mycursor.execute(sql)
        result = mycursor.fetchall()
        # Check if exists
        if len(result) == 0:
            abort(404, message="Trainee with the specified ID {} doesn't exist".format(
                trainee_id))
        else:
            # JSONify output
            result = [dict(zip([key[0] for key in mycursor.description], row))
                      for row in result]
        return result

    def delete(self, trainee_id):
        sql = '{0} {1}'.format(
            "DELETE FROM TraineeList WHERE ID =", trainee_id)
        mycursor.execute(sql)
        mydb.commit()
        # fix AUTO_INCREMENT value
        sql = "SELECT MAX(ID) FROM TraineeList"
        mycursor.execute(sql)
        max_id = str(mycursor.fetchall()[0])
        max_id = re.sub('[(),]', '', max_id)
        sql = '{0} {1}'.format(
            "ALTER TABLE TraineeList AUTO_INCREMENT = ", max_id)
        mycursor.execute(sql)
        return '{0} {1}'.format("1", "record(s) deleted"), 200

    def put(self, trainee_id):
        args = parser.parse_args()
        # update only if arg value is not null
        Trainee.get(self, trainee_id)
        for param in args:
            if args[param] is not None:
                sql = 'UPDATE TraineeList SET {0} = "'"{1}"'" WHERE ID={2}'.format(
                    param, args[param], trainee_id)
                mycursor.execute(sql)
                mydb.commit()
        print(mycursor.rowcount, "record(s) affected")
        return 201
