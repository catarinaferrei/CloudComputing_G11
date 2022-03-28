import os
import grpc
import unittest
from car_pb2 import *
from car_pb2_grpc import CarStub
from carsbd import app
import carsbd
car_channel = grpc.insecure_channel("locahost:5000")
car_client = CarStub(car_channel)

class MyTestCase(unittest.TestCase):

    def test_get_car(self):
        with app.app_context():
            c = carsbd.get_car(1)
            self.assertEqual(c, 1)

    def test_createcar(self):
        with app.app_context():
            c = carsbd.create_car()
            qtdCar = c.__len__();
            self.assertEqual(qtdCar, 3)

    #def test_read_filtered(self):
    #    c = carsbd.
    #    qtdCar = c.__len__();
    #    self.assertEqual(qtdCar, 1)
    
    def test_get_cars(self):
        with app.app_context():
            c = carsbd.get_cars()
            self.assertEqual(qtdCar, 1)
    
    def test_CarData(self):
        with app.app_context():
            car_request = CarRequest(car_id=1)
            self.assertEqual(len(car_client.CarData(car_request).car))

if __name__ == '__main__':
    unittest.main()
