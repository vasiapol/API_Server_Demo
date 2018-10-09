curl -k https://192.168.103.240/
curl -k https://192.168.103.240/api/v1/trainees
curl -k https://192.168.103.240/api/v1/trainees/5
curl -k -X POST -d "Firstname=Demo1&Lastname=Demo1&Age=10&Married=NO" https://192.168.103.240/api/v1/trainees
curl -k -X PATCH -d Firstname=test https://192.168.103.240/api/v1/trainees/
curl -k https://192.168.103.240/api/v1/trainees
curl -k -X DELETE https://192.168.103.240/api/v1/trainees/29
curl -k https://192.168.103.240/api/v1/trainees
while true;do mysql -u haproxy_check -h 192.168.103.240 -P 32596 -e 'select @@hostname;'|grep galera && sleep 1;done
while true;do curl http://192.168.103.240:30005/ && sleep 1;done
