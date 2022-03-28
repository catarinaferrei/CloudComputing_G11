from concurrent import futures
from distutils.log import debug
import grpc
from grpc_interceptor.exceptions import NotFound
from grpc_interceptor import ExceptionToStatusInterceptor
from carsbd import Car, app
from flask import jsonify
from config import db
from car_pb2 import (
    CarRequest,
    CarData,
    CarIdResponse
)
import car_pb2_grpc

def get_car_list(id):
  car_list = db.session.query(Car).filter_by(car_id=id).first()
  return jsonify(car_list.__dict__)

def get_car_id(id):
  carid = Car.query.get(id)
  return jsonify(carid.__dict__)

class CarService(car_pb2_grpc.CarServicer):
    
    def Car(self, request, context):
        """
    Args:
        param_init: gets a car id 
        returns: a car
    """
        car_data = get_car_list(request.car_id) 
        if car_data is None:
            raise NotFound("car not found")

        return CarRequest(car=CarData)

    def CarId(self, request, context):
        """
    Args:
        param_init: gets a car id 
        returns: returns car id
    """
        car_data = get_car_id(request.car_id)
        if car_data is None:
            raise NotFound("carid not found")

        return CarRequest(car=CarIdResponse)
    
    

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