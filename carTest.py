from server import app

import unittest, cars


class MyTestCase(unittest.TestCase):

    def test_readMovie(self):
        m = cars.read_one(1)
        idMovie = m.get('tconst');
        self.assertEqual(idMovie, 1)

    def test_readAll(self):
        m = cars.read_all()
        qtdMovie = m.__len__();
        self.assertEqual(qtdMovie, 20)

    def test_read_filtered(self):
        m = cars.read_filtered('Carmencita', 'Documentary', 'US', '', '1894')
        qtdMovie = m.__len__();
        self.assertEqual(qtdMovie, 1)

if __name__ == '__main__':
    unittest.main()
