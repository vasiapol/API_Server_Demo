
curl http://192.168.0.100:5000/
curl http://192.168.0.100:5000/api/v1/trainees
curl http://192.168.0.100:5000/api/v1/trainees/<id>
curl -X DELETE http://192.168.0.100:5000/api/v1/trainees/<id>
curl -X POST -d "Firstname=test&Lastname=test&Age=10" http://192.168.0.100:5000/api/v1/trainees
curl -X PUT -d Firstname=test http://192.168.0.100:5000/api/v1/trainees/<id>
while true;do mysql -u haproxy_check -h 192.168.103.240 -P 32596 -e 'select @@hostname;'|grep galera && sleep 1;done
while true;do curl --insecure https://192.168.103.240/ && sleep 1;done
