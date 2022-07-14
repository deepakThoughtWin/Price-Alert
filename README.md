# PRICE_ALERT

   


### PROJ DESCRIPTION ---->
  
   Sending Alert when user defined  price reached,
   
   In this we are Using -      
   (1) Django.
    (2) Django Rest API
    (3) Celery.
    (4) Sqlite.
    (5) Docker.


### Required Packages ---->  
   
   For Price Alert --> 
   (1) Django==4.0.6 
    (2) celery==5.2.7  
    (3) redis==4.3.4
    (4) redis-server==6.0.9
                       
### RUN Using Docker ---->
  
    (1) sudo docker-compose up                             // for start the application


### For Generate Access Token endpoint API --->

    post method -->    http://0.0.0.0:8000/api/token/ 
                                                        (1) username = admin
                                                        (2) password = 123


### For Alert And Filter endpoint API  --->

    get method -->     http://0.0.0.0:8000/api/alert/get/
                                                        (#) Bearer Token  


### For Create Alert endpoint API  --->

    post method -->    http://0.0.0.0:8000/api/alert/create/
                                                        (#) Bearer Token 
   

### For Delete Alert endpoint API  --->

    delete method -->  http://0.0.0.0:8000/api/alert/delete/{alert_id}/
                                                        (#) Bearer Token    

###Just Use Postman Collection by importing it

   
    postman_collection.json

### Create .env file  --->

  For Secure variables --> 
  (1) HOST
    (2) PASSWORD
    (3) DockerHOME

### Email Sending ---->
      
      BY (Gmail SMTP) -->
                        (1) EMAIL_PORT = 465
                        (2) EMAIL_HOST_USER = ""
                        (3) EMAIL_HOST_PASSWORD = ""