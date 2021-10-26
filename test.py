import unittest
from unittest import TestCase
from DZ__3 import GeometricCalculator
from DZ__3 import FlatFigures
from DZ__3 import VolumetricFigures

'''Класс для проверки GeometricCalculator'''
'''If input data appears during the check, designate the variable equal to one'''

class TestStringMethods(TestCase):

    ''' Methods for calculating the area of flat figures and volumetric figures '''

    def test_area_square(self):
        self.calculate = FlatFigures('квадрат')
        self.calculate.sides = [4.0]
        self.assertEqual(self.calculate.area(), 16.0)

    def test_area_rectangle(self):
        self.calculate = FlatFigures('прямоугольник')
        self.calculate.sides = [4.0, 5.0]
        self.assertEqual(self.calculate.area(), 20.0)

    def test_area_triangle(self):
        self.calculate = FlatFigures('треугольник')
        self.calculate.sides = [5.0, 5.0, 6.0]
        self.assertEqual(self.calculate.area(), 4.8)

    def test_area_trapezoid(self):
        self.calculate = FlatFigures('трапеция')
        self.calculate.sides = [6.0, 12.0, 8.0, 10.0]
        self.assertEqual(self.calculate.area(), 72.0)

    def test_area_rhombus(self):
        self.calculate = FlatFigures('ромб')
        self.calculate.sides = [6.0]
        self.calculate.diagonal = [3.0, 4.0]
        self.assertEqual(self.calculate.area(), 6.0)

    def test_area_circle(self):
        self.calculate = FlatFigures('круг')
        self.calculate.radius = [1]
        self.assertEqual(self.calculate.area(), 3.14)

    def test_area_cube(self):
        self.calculate = VolumetricFigures('куб')
        self.calculate.sides = [4.0]
        self.assertEqual(self.calculate.area(), 96.0)

    def test_area_parallelepiped(self):
        self.calculate = VolumetricFigures('параллелепипед')
        self.calculate.sides = [3.0, 4.0, 5.0]
        self.assertEqual(self.calculate.area(), 94.0)

    def test_area_pyramid(self):
        self.calculate = VolumetricFigures('пирамида')
        self.calculate.areas = [25.0, 20.0]
        self.assertEqual(self.calculate.area(), 45.0)

    def test_area_cylinder(self):
        self.calculate = VolumetricFigures('цилиндр')
        self.calculate.radius= [3.0]
        self.calculate.h = [5.0]
        self.assertEqual(self.calculate.area(), 150.72)

    def test_area_cone(self):
        self.calculate = VolumetricFigures('конус')
        self.calculate.radius = [3.0]
        self.calculate.h = [4.0]
        self.assertEqual(self.calculate.area(), 75.36)

    def test_area_sphere(self):
        self.calculate = VolumetricFigures('шар')
        self.calculate.radius = [2.0]
        self.assertEqual(self.calculate.area(), 50.24)

    ''' Method for calculating the perimeter of flat figures and volumetric figures '''
    def test_perimeter_square(self):
        self.calculate = FlatFigures('квадрат')
        self.calculate.sides = [4.0]
        self.assertEqual(self.calculate.perimeter(), 16.0)

    def test_perimeter_rectangle(self):
        self.calculate = FlatFigures('прямоугольник')
        self.calculate.sides = [4.0, 5.0]
        self.assertEqual(self.calculate.perimeter(), 18.0)

    def test_perimeter_triangle(self):
        self.calculate = FlatFigures('треугольник')
        self.calculate.sides = [5.0, 5.0, 6.0]
        self.assertEqual(self.calculate.perimeter(), 16.0)

    def test_perimeter_trapezoid(self):
        self.calculate = FlatFigures('трапеция')
        self.calculate.sides = [6.0, 12.0, 8.0, 10.0]
        self.assertEqual(self.calculate.perimeter(), 36.0)

    def test_perimeter_rhombus(self):
        self.calculate = FlatFigures('ромб')
        self.calculate.sides = [2.0]
        self.assertEqual(self.calculate.perimeter(), 8.0)

    def test_perimeter_circle(self):
        self.calculate = FlatFigures('круг')
        self.calculate.radius = [3]
        self.assertEqual(self.calculate.perimeter(), 18.84)

    ''' Method for calculating the volume of flat figures and volumetric figures '''

    def test_volume_cube(self):
        self.calculate = VolumetricFigures('куб')
        self.calculate.sides = [3.0]
        self.assertEqual(self.calculate.volume(), 27.0)

    def test_volume_parallelepiped(self):
        self.calculate = VolumetricFigures('параллелепипед')
        self.calculate.sides = [3.0, 4.0, 5.0]
        self.assertEqual(self.calculate.volume(), 60.0)

    def test_volume_cylinder(self):
        self.calculate = VolumetricFigures('цилиндр')
        self.calculate.radius = [3.0]
        self.calculate.h = [5.0]
        self.assertEqual(self.calculate.volume(), 141.3)

    def test_volume_cone(self):
        self.calculate = VolumetricFigures('конус')
        self.calculate.radius = [3.0]
        self.calculate.h = [4.0]
        self.assertEqual(self.calculate.volume(), 37.68)

    def test_volume_sphere(self):
        self.calculate = VolumetricFigures('шар')
        self.calculate.radius = [3.0]
        self.assertEqual(self.calculate.volume(), 113.04)

    def test_volume_pyramid(self):
        self.calculate = VolumetricFigures('пирамида')
        self.calculate.areas = [21.0]
        # h = 1
        self.assertEqual(self.calculate.volume(), 7.0)

    ''' Method for calculating the diameter of flat figures and volumetric figures '''

    def test_diameter(self):
        self.calculate = GeometricCalculator('круг')
        # radius = 1
        self.assertEqual(self.calculate.diameter(), 2.0)

    ''' Methods for calculating the circumference of volumetric figures '''

    def test_circumference(self):
        # radius_circle = 1
        self.calculate = VolumetricFigures('шар')
        self.assertEqual(self.calculate.circumference(), 6.28)


if __name__ == '__main__':
    unittest.main()
