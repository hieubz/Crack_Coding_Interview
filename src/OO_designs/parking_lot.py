import unittest


class Car:
    pass


class ParkingLot(object):
    def __init__(self):
        self.cars = {}

    def park_car(self, car):
        self.cars[car] = True

    def unpark_car(self, car):
        del self.cars[car]


class Test(unittest.TestCase):
    def test_parking_lot(self):
        plot = ParkingLot()
        car1 = Car()
        car2 = Car()
        plot.park_car(car1)
        plot.park_car(car2)
        self.assertEqual(len(plot.cars), 2)


if __name__ == '__main__':
    unittest.main()
