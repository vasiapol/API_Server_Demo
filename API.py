import os
from flask import Flask
from flask_restful import Api
from functionality import welcome, trainee, trainee_list



app = Flask(__name__)
api = Api(app)


##
# Actually Api resource routing here
##
api.add_resource(trainee_list.TraineeList, '/api/v1/trainees')
api.add_resource(trainee.Trainee, '/api/v1/trainees/<trainee_id>')
api.add_resource(welcome.Welcome, '/')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
