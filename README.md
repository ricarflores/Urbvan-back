# Urbvan-back
Back end for urvban test
## Requeriments
  - python3
  - pip3
## Install Dependencies
   - pip install -r requirements.txt
   - python3 -m pip install pymongo[srv]
## Start Server
  - python3 app.py

## For test end point
    - Use postman collection to access to the endpoint
 
| EndPoint | Type | Body/Parmas  |
| ------------- | ------------- | ------------- |
| GetAllUsers  | GET  | page, limit  | 
| CreateUser | POST  | name, last_name  |
| UpdateUser | PATCH  | id, name, last_name  |
| DeleteUser | DELETE  | id  |
