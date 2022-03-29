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
)
import car_pb2_grpc

def get_car_list(id):
 car_list = db.session.query(Car).filter_by(carid=id).first()
 if car_list is not None:
    del car_list.__dict__['_sa_instance_state']
    return jsonify(car_list.__dict__)
 else:
    abort(409, f'User preferences dont exist')


class CarService(car_pb2_grpc.CarServicer):
    
    def CarSearch(self, request):
        """
    Args:
        param_init: gets a car id 
        returns: a car
    """
        car_data = get_car_list(request.car_id) 
        if car_data is None:
            raise NotFound("car not found")

        return CarRequest(cars=CarDataResponse)



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