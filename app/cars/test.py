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
    def test_car_by_id(self):
        with app.app_context():
            service = CarService()
            request = CarRequestID(car_id=1)
            response = service.CarSearch(request)
            #print(type(response.cars))
            self.assertEquals(response.cars.car_id, 1)
            #assert len(response.cars) == 1
    def test_get_car_data(self):
        with  app.app_context():
            service = CarService()
            request = CarRequest(region='NY')
            response = service.GetCarData(request)
            self.assertEquals(response.cars.region, 'NY')

    def test_get_car_by_manufacturer(self):
        with  app.app_context():
            service = CarService()
            request = SearchByManufacturerRequest(manufacturer='Farrell')
            response = service.SearchByManufacturer(request)
            self.assertEquals(response.cars.manufacturer, 'Farrell')
    
    def test_get_car_by_model(self):
        with  app.app_context():
            service = CarService()
            request = SearchByModelRequest(model='Farrell')
            response = service.SearchByModel(request)
            self.assertEquals(response.cars.model, 'Farrell4')

            


  

if __name__ == '__main__':
    unittest.main()
