# Mizuho Investment Technology 2022 Quiz
## API Documentation

### Overview
All the endpoints for this quiz start with http://127.0.0.1:8000/. 
In total there are 3 endpoints: 
1.	http://127.0.0.1:8000/register
2.	http://127.0.0.1:8000/login
3.	http://127.0.0.1:8000/getuser
4.	http://127.0.0.1:8000/delete

IMPORTANT:
Before you may use the other endpoints, you must first register with the proper endpoint.

### 1. Register

Endpoint: http://127.0.0.1:8000/register
POST /register
Content-Type: x-www-form-urlencoded

|      Parameter     |      Type     |      Required?     |      Description                                                              |
|--------------------|---------------|--------------------|-------------------------------------------------------------------------------|
|     email          |     string    |     required       |     The email address   is used to register with the database.                |
|     password       |     string    |     required       |     The password is being   utilised for login and other functionalities.     |
|     name           |     string    |     required       |     The name of the   user.                                                   |




Possible HTTP status:
|      Code     |      Description                                                                                     |
|---------------|------------------------------------------------------------------------------------------------------|
|     200       |     No fault. Data   has been added to the database without any difficulties.                        |
|     400       |     Invalid input or   system issue. For further details can refer accompanied with the response.    |
|     name      |     string                                                                                           |

Example:<br>
```
Request to: 
POST http://127.0.0.1:8000/register 
{ 
	“email”: test2@test2.com, 
	“password”: test2, 
	“name”: test2 
}
```
Response: 
```
Status 200 OK 
{ 
    "message": "User registered", 
    "success": true 
} 
```


### 2. Login
Endpoint: http://127.0.0.1:8000/login
POST /login
Content-Type: x-www-form-urlencoded

|      Parameter     |      Type     |      Required?     |      Description                                                                            |
|--------------------|---------------|--------------------|---------------------------------------------------------------------------------------------|
|     email          |     string    |     required       |     The email address   is used to check whether such an account exists in the database.    |
|     password       |     string    |     required       |     The password is used   for authorised entry.                                            |

Possible HTTP status:
|      Code     |      Description                                                                                     |
|---------------|------------------------------------------------------------------------------------------------------|
|     200       |     No fault. Data   has been added to the database without any difficulties.                        |
|     400       |     Invalid input or   system issue. For further details can refer accompanied with the response.    |
|     404       |     In case the email   or/and password is wrong.                                                    |

Example: <br>
Request to:
```
POST http://127.0.0.1:8000/login
{
	“email”: test2@test2.com,
	“password”: test2,
}
```
Response:
```
Status 200 OK
{
    "message": "Logged in.",
    "success": true,
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY0NTk4NDg5MiwianRpIjoiMWQ5ZjYyNjUtNzZkOC00MzYwLWFjZTUtZjdjMzY2NTFlMDA2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6NCwibmJmIjoxNjQ1OTg0ODkyLCJleHAiOjE2NDU5OTIwOTJ9.WCAUb8X7BpHdMa8Ua8cxqYne_uYnsr5tt8tRHSCH6h8"
}
```

### 3. Get User Information

For using this API, the JWT token is required. This endpoint can be used after logging in.

Endpoint: http://127.0.0.1:8000/getuser
GET /getuser
Content-Type: headers
|      Parameter       |      Type     |      Required?     |      Description                                                                            |
|----------------------|---------------|--------------------|---------------------------------------------------------------------------------------------|
|     Authorization    |     string    |     required       |     JWT token is   passed through the header for receiving the information for the user.    |

Possible HTTP status:
|      Code     |      Description                                                                                     |
|---------------|------------------------------------------------------------------------------------------------------|
|     200       |     No fault. Data   has been added to the database without any difficulties.                        |
|     400       |     Invalid input or   system issue. For further details can refer accompanied with the response.    |

Example:
```
Request to: 
GET http://127.0.0.1:8000/getuser
{
	“Authorization”: “Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY0NTk4NDg5MiwianRpIjoiMWQ5ZjYyNjUtNzZkOC00MzYwLWFjZTUtZjdjMzY2NTFlMDA2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6NCwibmJmIjoxNjQ1OTg0ODkyLCJleHAiOjE2NDU5OTIwOTJ9.WCAUb8X7BpHdMa8Ua8cxqYne_uYnsr5tt8tRHSCH6h8”
}
```

Response:
```
Status 200 OK
{
    "message": [
        {
            "email": "test3@test3.com",
            "name": "test3",
            "password": "test3",
            "user_id": 4
        }
    ],
    "success": true
}
```

### 4. Delete an Account

For using this API, the JWT token is required. Only the Admin can make use of this endpoint.

Endpoint: http://127.0.0.1:8000/delete
GET /delete
Content-Type: headers

|      Parameter       |      Type     |      Required?     |      Description                                                                            |
|----------------------|---------------|--------------------|---------------------------------------------------------------------------------------------|
|     Authorization    |     string    |     required       |     JWT token is   passed through the header for receiving the information for the user.    |
|     email            |     string    |     required       |     Used to specify   which account has to be deleted.                                      |

Possible HTTP status:
|      Code     |      Description                                                                                                                         |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------|
|     200       |     No fault. Data   has been added to the database without any difficulties.                                                            |
|     400       |     Invalid input or   system issue. For further details can refer accompanied with the response.                                        |
|     404       |     This error takes   place when the admin has not logged in, the account does not exist or admin   email is sent through parameter.    |

Example:
```
Request to: 
GET http://127.0.0.1:8000/delete
Headers:
{
	“Authorization”: “Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY0NTk4NDg5MiwianRpIjoiMWQ5ZjYyNjUtNzZkOC00MzYwLWFjZTUtZjdjMzY2NTFlMDA2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6NCwibmJmIjoxNjQ1OTg0ODkyLCJleHAiOjE2NDU5OTIwOTJ9.WCAUb8X7BpHdMa8Ua8cxqYne_uYnsr5tt8tRHSCH6h8”
}
body:
{
	“email”: “test3@test3.com”
}
```
Response:
```
Status 200 OK
{
    "message": [
        {
            Account of test3 deleted.
        }
    ],
    "success": true
}
```
