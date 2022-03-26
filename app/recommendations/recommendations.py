import os
from turtle import color

from flask import Flask, render_template
import grpc



#from protofbuf cliente import ....
#from protobuf cars import ....
#from ... import UserStub, CarsStub, UserRequest, CarsRequest


app = Flask(__name__)

#user_host = os.getenv("USER_HOST", "localhost") ?*?
#cars_host = os.getenv("CARS_HOST", "localhost") ?*?

#with open("client.key", "rb") as fp:
#    client_key = fp.read()
#with open("client.pem", "rb") as fp:
#    client_cert = fp.read()
#with open("ca.pem", "rb") as fp:
#    ca_cert = fp.read()
#creds = grpc.ssl_channel_credentials(ca_cert, client_key, client_cert)

user_channel = grpc.insecure_channel(f"{user_host}:50051")
user_client = UserStub(user_channel)

cars_channel = grpc.insecure_channel(f"{cars_host}:50051")
cars_client = CarsStub(cars_channel)


@app.route("/recomendations/<userId>")
def render_homepage():

    #user = UserInfo(userId)
    #listCars = Cars(user.preferences)

    user_request = UserRequest(
        user_id=userId
    )
    user_response = user_client.GetPrefferedSpecs(
        user_request
    )

    cars_request = CarsRequest(
        #color=user_response.color, brand=user_response.brand ......
    )
    cars_response = cars_client.GetListOfCars(
        cars_request
    )

    return render_template(
        "carsRecommendations.html",
        listCarsView = cars_response.list,
    )