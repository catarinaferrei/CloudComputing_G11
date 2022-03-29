from concurrent import futures
from distutils.log import debug
import grpc
from grpc_interceptor.exceptions import NotFound
from grpc_interceptor import ExceptionToStatusInterceptor
from carsbd import Car, app
from flask import jsonify, abort
from config import db
from car_pb2 import (
    CarRequest,
    CarDataResponse,
    CarData
)
import car_pb2_grpc

def get_car_by_id(id):
 car = db.session.query(Car).filter_by(carid=id).first()
 if car is not None:
    del car.__dict__['_sa_instance_state']
    #print(type(jsonify(car_list.__dict__)))
    return car_to_proto(car)
 else:
    abort(409, f'Car doesnt exist')

def car_to_proto(result):
    protocar = CarData (
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