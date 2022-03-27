import os
from turtle import color

from flask import Flask, render_template
import grpc

from user_pb2 import UserRequest
from user_pb2_grpc import UserStub

app = Flask(__name__)

user_host = os.getenv("USER_HOST", "localhost")
#cars_host = os.getenv("CARS_HOST", "localhost")

user_channel = grpc.insecure_channel(f"{user_host}:50055")
user_client = UserStub(user_channel)

#cars_channel = grpc.insecure_channel(f"{cars_host}:50051")
#cars_client = CarsStub(cars_channel)


@app.route("/recomendations/<userId>")
def render_homepage(userId):

    user_request = UserRequest(
        user_id=userId
    )
    user_response = user_client.GetPrefferedSpecs(
        user_request
    )
    
    #cars_request = CarsRequest(
        #color=user_response.color, brand=user_response.brand ......
    #)
    #cars_response = cars_client.GetListOfCars(
        #cars_request
    #)

    return user_response   