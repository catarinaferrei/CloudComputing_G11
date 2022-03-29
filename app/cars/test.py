import os
import grpc
import unittest
from car_pb2 import *
from car_pb2_grpc import CarStub
from cars import CarService, app

car_host = os.getenv("CAR_HOST", "localhost")
car_channel = grpc.insecure_channel(f"{car_host}:5000")
car_client = CarStub(car_channel)

class MyTestCase(unittest.TestCase):
    def test_recommendations(self):
        with app.app_context():
            service = CarService()
            request = CarRequest(car_id=1)
            response = service.CarSearch(request)
            assert len(response.cars) == 1

  

if __name__ == '__main__':
    unittest.main()
