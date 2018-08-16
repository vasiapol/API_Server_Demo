# Simple RESTful API server
## About this project
 This repository contains source code of the simple API server which allows retrieving, adding, modifying and deleting entries from MySQL database table.
## Functionality
### 1. Show all
Returns json data about all trainees
* URL
    `/api/v1/trainees`

* Method:
    `GET`
*  Success Response:
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

*  Success Response:

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

  Required:

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
