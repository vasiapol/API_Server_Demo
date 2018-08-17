
curl http://192.168.0.100:5000/
curl http://192.168.0.100:5000/api/v1/trainees
curl http://192.168.0.100:5000/api/v1/trainees/<id>
curl -X DELETE http://192.168.0.100:5000/api/v1/trainees/<id>
curl -X POST -d "Firstname=test&Lastname=test&Age=10" http://192.168.0.100:5000/api/v1/trainees
curl -X PUT -d Firstname=test http://192.168.0.100:5000/api/v1/trainees/<id>
