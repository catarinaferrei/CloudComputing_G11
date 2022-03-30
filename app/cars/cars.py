from concurrent import futures
from distutils.log import debug
import grpc
from grpc_interceptor.exceptions import NotFound
from grpc_interceptor import ExceptionToStatusInterceptor

from flask import Flask, jsonify, abort
#from config import db
from car_pb2 import (
    CarDataList,
    CarDataResponse,
    CarRequest)
import car_pb2_grpc
import os
import connexion
from flask_sqlalchemy import SQLAlchemy

USERNAME ='postgres'
PASSWORD ="canada12"
PUBLIC_IP_ADDRESS ="127.0.0.1"
DBNAME ="postgres"
PROJECT_ID ="cnprojext"
INSTANCE_NAME ="cn-projecto"


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))


# Create the Connexion application instance
connex_app = connexion.App(__name__, specification_dir=basedir)
#Line 9 uses the basedir variable to create the Connexion app instance and give it the path to the swagger.yml file.

# Get the underlying Flask app instance
app = connex_app.app

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://{0}:{1}@{2}/{3}".format(USERNAME, 
        PASSWORD,
        PUBLIC_IP_ADDRESS, DBNAME)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

print("---------",type(app))
# Create the SQLAlchemy db instance


def get_car_by_id(id):
 car = db.session.query(Car).filter_by(carid=id).first()
 if car is not None:
    del car.__dict__['_sa_instance_state']
    #print(type(jsonify(car_list.__dict__)))
    return car_to_proto(car)
 else:
    abort(409, f'Car doesnt exist')

def get_car_data(id,region, price, year, manufacturer,model,condition):
    car = []
    query = db.session.query(Car) 
    if id:
        query = query.filter(Car.carid==id)

    if region:
        query = query.filter(Car.region==region)
    if price: 
        query = query(Car).filter_by(price=price).first()
    if year:
        query = query(Car).filter_by(year=year).first()
    if manufacturer:
        query = query(Car).filter_by(manufacturer=manufacturer).first()
    if model:
        query = query(Car).filter_by(model=model).first()
    if condition:
        query = query(Car).filter_by(condition=condition).first()
    
    for data in query.limit(30).all():
        del data.__dict__['_sa_instance_state']
        car.append(data.__dict__)

    if car is not None:
        #del car.__dict__['_sa_instance_state']
        return car_to_proto(car)
    else:
        abort(409, f'Car doesnt exist')
    


def get_car_by_id_list(id):
 car = db.session.query(Car).filter_by(carid=id)
 if car is not None:
    del car.__dict__['_sa_instance_state']
    #print(type(jsonify(car_list.__dict__)))
    return car_to_proto(car)
 else:
    abort(409, f'Car doesnt exist')

def get_car_by_manufacturer(manufacturer):
 car = db.session.query(Car).filter_by(manufacturer=manufacturer).first()
 if car is not None:
    del car.__dict__['_sa_instance_state']
    #print(type(jsonify(car_list.__dict__)))
    return car_to_proto(car)
 else:
    abort(409, f'Manufacturer doesnt exist')

def get_car_by_price(price):
 car = db.session.query(Car).filter_by(price=price)
 if car is not None:
    del car.__dict__['_sa_instance_state']
    #print(type(jsonify(car_list.__dict__)))
    return car_to_proto(car)
 else:
    abort(409, f'Manufacturer doesnt exist')

def get_car_by_model(model):
 car = db.session.query(Car).filter_by(model=model)
 if car is not None:
    del car.__dict__['_sa_instance_state']
    #print(type(jsonify(car_list.__dict__)))
    return car_to_proto(car)
 else:
    abort(409, f'Model doesnt exist')

def get_car_by_region(region):
    car = db.session.query(Car).filter_by(region=region)
    if car is not None:
        del car.__dict__['_sa_instance_state']
    #print(type(jsonify(car_list.__dict__)))
        return car_to_proto(car)
    else:
        abort(409, f'Model doesnt exist')

def get_car_by_condition(condition):
    car = db.session.query(Car).filter_by(condition=condition)
    if car is not None:
        del car.__dict__['_sa_instance_state']
    #print(type(jsonify(car_list.__dict__)))
        return car_to_proto(car)
    else:
        abort(409, f'condition doesnt exist')

def get_car_by_year(year):
    car = db.session.query(Car).filter_by(year=year)
    if car is not None:
        del car.__dict__['_sa_instance_state']
    #print(type(jsonify(car_list.__dict__)))
        return car_to_proto(car)
    else:
        abort(409, f'year doesnt exist')


def car_to_proto(result):
    protocar = CarRequest (
        car_id = result.carid,
        region = result.region,
        price = result.price ,
        year = result.year ,
        manufacturer = result.manufacturer,
        model = result.model,
        condition = result.condition
    )
    return protocar

def proto_to_car(proto):
    car = {
            'carid' : proto.car_id,
            'region': proto.region,
            'price' : proto.price,
            'year' : proto.year,
            'manufacturer' :proto.manufacturer,
            'model' : proto.model,
            'condition' : proto.condition
    }
    
    return car

class CarService(car_pb2_grpc.CarServicer):
    
    def CarSearch(self, request):
        """
    Args:
        param_init: gets a car id 
        returns: a car
    """
        car_data = get_car_by_id(request.car_id) 
        if car_data is None:
            raise NotFound("car not found")

        return CarDataResponse(cars=car_data)
    
    def GetCarData(self, request):
        car_data = get_car_data(request.car_id,request.region, request.price, request.year, request.manufacturer,request.model,request.condition)
        if car_data is None:
            raise NotFound("car not found")

        return CarDataList(cars=car_data)
    def SearchById(self, request):
        """
    Args:
        param_init: car_id
        returns: returns a list of the car corresponding to car_id
        
        """
        car_data = get_car_by_id_list(request.car_id) 
        if car_data is None:
            raise NotFound("car not found")

        return CarDataList(cars=car_data)
    def SearchByManufacturer(self, request):
        """
    Args:
        param_init: request.manufacturer
        returns: returns a list of the cars corresponding to the manufacturer
        
        """
        car_data = get_car_by_manufacturer(request.manufacturer)
        if car_data is None:
            raise NotFound("car not found")
        return CarDataList(cars=car_data)
    def SearchByCondition(self, request):
        """
    Args:
        param_init: request.condition
        returns: returns a list of the cars corresponding to the condition
        
        """
        car_data = get_car_by_condition(request.condtion)
        return  CarDataList(cars=car_data)
    def SearchByYear(self, request):
        """
    Args:
        param_init: request.year
        returns: returns a list of the cars corresponding to the year

        """
        car_data = get_car_by_year(request.year)
        return CarDataList(cars=car_data)
    def SearchByModel(self, request):
        """
    Args:
        param_init: request.model
        returns: returns a list of the cars corresponding to the model
        
        """
        car_data = get_car_by_model(request.model)
        return CarDataList(cars=car_data)

    def SearchByRegion(self, request):
        """
    Args:
        param_init: request.region
        returns: returns a list of the cars corresponding to the region
        
        """
        car_data = get_car_by_region(request.region)
        return CarDataList(cars=car_data)



def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    car_pb2_grpc.add_CarServicer_to_server(
        CarService(), server
    )

    server.add_insecure_port("[::]:5000")
    server.start()
    server.wait_for_termination()



if __name__ == "__main__":

    app.run(debug=True)
    serve()

from carsbd import db, Car