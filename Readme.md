# Simple RESTful API server
## About this project
 This repository contains source code of the simple API server which allows retrieving, adding, modifying and deleting entries from MySQL database table.
## Install
### Deploy in Kubernetes cluster using makefile
#### Prerequisites
- Running kubernetes cluster
- Kubectl configured to perform deployment tasks
- You should be loggined in DockerHub

### Deployment guide

1.Clone this repo: 

 `git clone http://192.168.103.206:3000/Lv-335.DevOps/API_Server_Demo.git`

2.Change variable in Makefile

 ```
 name = api
 project = devops335
 ```




We're assumming that you're using CentOS and Python 2, so to run this project you have to complete following steps:
#### 1. Installation python-devel and gcc
 `sudo yum install gcc python-devel`
#### 2. Clone project\`s repository to your local machine
  `git clone http://192.168.103.236:3000/Lv-335.DevOps/API_Server_Demo.git`
#### 3. Go to the local copy of repository. Open terminal and run the following command
  `sudo pip install -r requirements.txt`
#### 4. Install and configure MariaDb or MySQL. Please check official guide:
* [MariaDb Installation guide ](https://mariadb.com/kb/en/library/getting-installing-and-upgrading-mariadb/)
* [MySQL Installation guide](https://dev.mysql.com/doc/refman/8.0/en/installing.html)

#### 5. Create database, table or even fill table with some data using appropriate scripts in project\`s sql folder.

#### 6. Update database configuration file db_conf.json with your settings
example:
```json
{   "db":{
      "host":"ip address",
      "user":"username",
      "passwd":"password",
      "database":"name"
   }
}
```
#### 7. Run project from local directory:
```bash
python API.py
```
## Functionality
### 1. Show all
Returns json data about all trainees
* URL
    `/api/v1/trainees`

* Method:
    `GET`
*  Successful Response:
  * Code: 200

    Content: `{ id:1, Firstname : "Name", Lastname : "Name", Age : "20" }`
* Error Response:
  * Code: 404 NOT FOUND

    Content: `{ Error : "Table is empty" }`

### 2. Show single trainee
Returns json data about trainee with the specified id
* URL
    `/api/v1/trainees/<id>`

* Method:
    `GET`
* URL Params

    Required:
    `id=[integer]`

*  Successful Response:

      * Code: 200

        Content: `{ id:1, Firstname : "Name", Lastname : "Test", Age : "20" }`
* Error Response:
    * Code: 404 NOT FOUND

      Content: `{ Error : "Trainee with the specified id <id> does not exist" }`

### 3. Delete single trainee
Deletes trainee with the specified id
* URL  `/api/v1/trainees/<id>`

* Method:
`DELETE`
* URL Params

  Required:
`id=[integer]`

*  Success Response:

  * Code: 200

    Content: `"1 record deleted"`
* Error Response:
  * Code: 404 NOT FOUND

    Content: `{ Error : "Trainee with the specified id <id> does not exist" }`

### 4. Add new trainee
Creates new  trainee
* URL  `/api/v1/trainees`

* Method:
    `POST`
* Data Params:

    RequiredD:

    `Firstname=[string]`

    `Lastname=[string]`

    `Age=[integer]`

*  Success Response:
    * Code: 201

        Content: `"Created"`
* Error Response:
    * Code: 400 BAD REQUEST

        Content: `{ Error : "Some values of parameters are empty" }`

### 5. Update single trainee
Updates one or more parameters of trainee with specified id
* URL  `/api/v1/trainees/<id>`

* Method: `PUT`
* URL Params

  Required:
`id=[integer]`

* Data Params:

    Required (one or more):

    `Firstname=[string]`

    `Lastname=[string]`

    `Age=[integer]`

*  Success Response:
    * Code: 201

    Content: `"1 record affected"`
* Error Response:
    * Code: 400 BAD REQUEST

        Content: `{ Error : "Values of parameters are empty" }`

        OR
    * Code: 404 NOT FOUND

       Content: `{ Error : "Trainee with the specified id <id> does not exist" }`
       
       uwsgi --http 0.0.0.0:5000 --module wsgi:app
       uwsgi --ini API.ini