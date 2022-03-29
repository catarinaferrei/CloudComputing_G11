import os

from flask import Flask, render_template
import grpc

from user_pb2 import UserRequest
from user_pb2_grpc import UsersStub

#from cars_pb2 import CarsRequest
#from cars_pb2_grpc import CarsStub

app = Flask(__name__)

user_host = os.getenv("USER_HOST", "localhost")
user_channel = grpc.insecure_channel(f"{user_host}:50055")
user_client = UsersStub(user_channel)

#cars_host = os.getenv("CARS_HOST", "localhost")
#cars_channel = grpc.insecure_channel(f"{cars_host}:5000")
#cars_client = CarsStub(cars_channel)

@app.route("/recommendations/<userId>")
def render_homepage(userId):

    user_request = UserRequest(
        user_id=userId
    )
    user_response = user_client.Preferences(
        user_request
    )
    
    #cars_request = CarsRequest(
        #car_id = user_response
        #region = user_response.region
        #price = user_response.price
        #year = user_response.year
        #manufacturer = user_response.manufacturer
        #model = user_response.model
        #condition = user_response.condition
        #car_id = 1
    #)
    #cars_response = cars_client.CarSearch(
        #cars_request
    #)

    return user_response
    #return cars_response
       