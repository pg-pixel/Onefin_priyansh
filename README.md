This Project is created by Priyansh Gautam (gautam.priyansh98@gmail.com)

If someone wants to use this, firt they have to register, then login.
Note: Login will generate jwt_token. Without that we will not be able to use other apis.

list of API and dummy payload :

1. POST-http://127.0.0.1:8000/register/
  payload = {
    "username" : "a",
    "email" : "a@a.com",
    "password" : "a"
    } 

  response = {
    "username": "a",
    "email": "a@a.com"
    }

2. POST - http://127.0.0.1:8000/login/
   payload ={
    "email":"a@a.com",
    "password": "a"
 }

  response = {
    "message": "Login succesful"
 }
  In the response cookies, we are having jwt_token .

3. GET - http://127.0.0.1:8000/movies/
   
4. POST - http://127.0.0.1:8000/collection/

  payload= {
    "title": "Collect1",
    "description": "Collection1",
    "movies": [
        {
            "header": "Hello",
            "description": "hello again",
            "genres": "A,B,C",
            "uuid": "550e8400-e29b-41d4-a716-446655440000"
        }
    ]
}

response = {
    "collection id": "430c8a43-b341-481c-8252-23348cee8431"
} 

5. GET- http://127.0.0.1:8000/collection/
 response = {
    "is_success": true,
    "data": {
        "collections": [
            {
                "id": "18715e5b-0bfb-4a2a-a0fb-01372855cdcf",
                "title": "Collect1",
                "description": "Collection1",
                "user": 1
            }
            
        ],
        "favorite_genres": "A, B, C"
    }
}
6. PUT- http://127.0.0.1:8000/collection/31361204-be2d-44ef-be01-8059ebb5d717/
 payload = {
    "title": "priyanhs",
    "description": "Gautam",
    "movies": [
        {
            "title": "Hello1",
            "description": "hello again1",
            "genres": "A,B,C",
            "uuid": "6ba7b810-9dad-11d1-80b4-00c04fd430c8"
        },
        {
            "title": "Hello3",
            "description": "hello again3",
            "genres": "A,B,C",
            "uuid": "c0a80121-7b2d-4ab3-97da-798c9c8440a1"
        }
    ] 
}
 response = {
    "title": "priyanhs",
    "description": "Gautam",
    "movies": [
        {
            "title": "Hello1",
            "description": "hello again1",
            "genres": "A,B,C",
            "uuid": "6ba7b810-9dad-11d1-80b4-00c04fd430c8"
        },
        {
            "title": "Hello3",
            "description": "hello again3",
            "genres": "A,B,C",
            "uuid": "c0a80121-7b2d-4ab3-97da-798c9c8440a1"
        }
    ]
}

7. DELETE -http://127.0.0.1:8000/collection/e0ff2de7-6f49-4e74-b0f4-246d541546df/ 

8. POST - http://127.0.0.1:8000/request/reset/

9. GET - http://127.0.0.1:8000/collection/b93ba1c9-0e46-474b-9183-c3dedf36c85d/ 

10. GET - http://127.0.0.1:8000/request/