from server import app

import unittest, cars


class MyTestCase(unittest.TestCase):

    def test_readCar(self):
        c = cars.read_one(1)
        idCar = c.get('carid');
        self.assertEqual(idCar, 1)

    def test_readAll(self):
        c = cars.read()
        qtdCar = c.__len__();
        self.assertEqual(qtdCar, 3)

    def test_read_filtered(self):
        c = cars.read_filtered('NY', 3000, '2014', 'Farrell', 'Farrell4', 'good')
        qtdCar = c.__len__();
        self.assertEqual(qtdCar, 1)

if __name__ == '__main__':
    unittest.main()
