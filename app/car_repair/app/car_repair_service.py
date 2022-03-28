from concurrent import futures
import random

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

import car_repair_service_pb2_grpc

PORT = "5001"

#Service
class CarRepairService( ):
    def Add(self, request, context):
        ##TODO: Add car to repair to database and set status WAITING_CHECKUP
        return AddResponse(car_id=1)

    def GetRepairStatus ( self, request, context ):
        ##TODO: Read status from database and deliver
        return StatusResponse(car_id=1, status = CarRepairStatus.WAITING_CHECKUP)

    def UpdateStatus ( self, request, context ):
        ##TODO: Update car status in database
        return StatusUpdateResponse( car_id=1 ) )

    def Delete( self, request, context ):
        ##TODO: Delete car repair request
        return DeleteRepairRespose( car_id=1 )


##__RUN__##
def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )

    car_repair_service_pb2_grpc.add_CarRepairServiceServicer_to_server(
        CarRepairService(), server
    )

    server.add_insecure_port("[::]:"+PORT)
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
