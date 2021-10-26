import math
from functools import reduce
import sys
"""
Плоские фигуры: круг, квадрат, прямоугольник, треугольник, трапеция, ромб.
Объемные фигуры: сфера, куб, параллелепипед, пирамида, цилиндр, конус.
"""


''' Первая переменная словаря нужна для вычисления площади (для списка длин всех сторон).
Вторая переменная словаря нужна для расчета объема. '''

flat_figures = {'квадрат': [1, 4], 'прямоугольник': [2, 2], 'треугольник': [3, 1],
                'трапеция': [4, 1], 'ромб': [1, 4], 'круг': [1, 3.14]}

volumetric_figures = {'куб': [1, 6], 'параллелепипед': [3, 1], 'пирамида': [2, 1],
                      'цилиндр': [1, 3.14],'конус': [1, 3.14], 'шар': [1, 3.14]}


class GeometricCalculator():
    def __init__(self, name):
        self.name = name  # names of figures
        self.sides = []  # side length list
        self.h = []  # figure height list
        self.radius = []  # shape radius list
        self.diagonal = []  # list of diagonals of the figure
        self.areas = []  # list of area of the figure

    ''' Используемый ввод. '''

    def input_sides(self):
        for key, value in flat_figures.items():
            if self.name == key and key != 'ромб' and key != 'круг':
                self.sides = [float(input("Введите сторону " + str(i + 1) + " : ")) for i in
                              range(value[0])]  # type: list[float]
            if self.name == key:
                if key == 'ромб':
                    self.sides = [float(input("Введите сторону " + str(i + 1) + " : ")) for i in
                                  range(value[0])]  # type: list[float]
                    self.diagonal = [float(input("Введите диагональ " + str(i + 1) + " : ")) for i in
                                      range(value[1] - 2)]  # type: list[float]
                if key == 'круг':
                    self.radius = [float(input("Введите радиус " + str(i + 1) + " : ")) for i in
                                   range(value[0])]  # type: list[float]
        for key, value in volumetric_figures.items():
            if self.name == key and (key == 'куб' or key == 'параллелепипед'):
                self.sides = [float(input("Введите сторону " + str(i + 1) + " : ")) for i in
                              range(value[0])]  # type: list[float]
            if self.name == key and key == 'пирамида':
                self.areas = [float(input("Введите площадь " + str(i + 1) + " : ")) for i in
                              range(value[0])]  # type: list[float]
            if self.name == key and (key == 'цилиндр' or key == 'конус') and key != 'шар':
                self.radius = [float(input("Введите радиус " + str(i + 1) + " : ")) for i in
                               range(value[0])]  # type: list[float]
                self.h = [float(input("Введите высоту " + str(i + 1) + " : ")) for i in
                          range(value[0])]  # type: list[float]
            if self.name == key and key == 'шар':
                self.radius = [float(input("Введите радиус " + str(i + 1) + " : ")) for i in
                               range(value[0])]  # type: list[float]

    ''' Method for calculate diameter. '''

    @staticmethod
    def diameter():
        radius = float(input(('Введите радиус: ')))  # type: float
        d = 2 * radius  # type: float
        print(f'Диаметр равен {d}')
        return d


''' Класс для расчета площади и периметра плоских фигур. '''

class FlatFigures(GeometricCalculator):

    ''' метод расчета площади '''

    def area(self):
        if self.name == 'квадрат':
            area_s = self.sides[0] ** 2
            print(f'Площадь квадрата равна {area_s}')  # type: float
            return area_s
        if self.name == 'прямоугольник':
            area_s = reduce(lambda x, y: x * y, self.sides)
            print(f'Площадь прямоугольника равна {area_s}')  # type: float
            return area_s
        if self.name == 'треугольник':
            p = sum(self.sides) / 2
            area_s = (2 * (math.sqrt(p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2])))) / self.sides[
                0]  # type: float
            print(f'Площадь треугольника равна {area_s}')
            return area_s
        if self.name == 'трапеция':
            h = math.sqrt(self.sides[2] ** 2 - (
                    ((self.sides[0] - self.sides[1]) ** 2 + self.sides[2] ** 2 - self.sides[3] ** 2) / (
                    2 * (self.sides[0] - self.sides[1]))) ** 2)
            area_s = ((self.sides[0] + self.sides[1]) / 2) * h
            print(f'Площадь трапеции равна {area_s}')  # type: float
            return area_s
        if self.name == 'ромб':
            area_s = (self.diagonal[0] * self.diagonal[1]) / 2
            print(f'Площадь ромба равна {area_s}')  # type: float
            return area_s
        if self.name == 'круг':
            pi = 3.14
            area_s = pi * self.radius[0] ** 2
            print(f'Площадь круга равна {area_s}')  # type: float
            return area_s

    ''' Методика расчета периметра. '''

    def perimeter(self):
        for key, value in flat_figures.items():
            if self.name == key and key != 'круг':
                P = sum(self.sides) * value[1]
                print(f'Периметр {self.name}a равен {P}')  # type: float
                return P
            if self.name == key:
                if key == 'круг':
                    P = 2 * value[1] * self.radius[0]
                    print(f'Периметр {self.name}a равен {P}')  # type: float
                    return P


''' Класс для расчета площади и стоимости объемных фигур '''


class VolumetricFigures(GeometricCalculator):

    ''' Методика расчета площади. '''

    def area(self):
        for key, value in volumetric_figures.items():
            if self.name == key == 'куб':
                area_s = value[1] * self.sides[0] ** 2
                print(f'Площадь куба равна {area_s}')  # type: float
                return area_s
            if self.name == key == 'параллелепипед':
                area_s = 2 * (self.sides[0] * self.sides[1] + self.sides[1] * self.sides[2] + self.sides[0] * self.sides[
                    2])  # type: float
                print(f'Площадь параллелепипеда равна {area_s}')
                return area_s
            if self.name == key == 'пирамида':
                area_s = self.areas[0] + self.areas[1]
                print(f'Площадь пирамиды равна {area_s}')  # type: float
                return area_s
            if self.name == key == 'цилиндр':
                area_s = 2 * value[1] * (self.radius[0] ** 2) + 2 * value[1] * (self.radius[0] * self.h[0])
                print(f'Площадь цилиндра равна {area_s}')  # type: float
                return area_s
            if self.name == key == 'конус':
                area_s = value[1] * self.radius[0]*(self.radius[0]+(math.sqrt(self.radius[0] ** 2 + self.h[0] ** 2)))  # type: float
                print(f'Площадь конуса равна {area_s}')
                return area_s
            if self.name == key == 'шар':
                area_s = 4 * value[1] * self.radius[0] ** 2
                print(f'Площадь шара равна {area_s}')  # type: float
                return area_s

    ''' Методика расчета объема. '''

    def volume(self):
        for key, value in volumetric_figures.items():
            if self.name == key == 'куб':
                v = self.sides[0] ** 3
                print(f'Объем {self.name}a равен {v}')  # type: float
                return v
            if self.name == key == 'параллелепипед':
                v = reduce(lambda x, y: x * y, self.sides)
                print(f'Объем {self.name}a равен {v}')  # type: float
                return v
            if self.name == key and key == 'пирамида':
                h = float(input(' Необходимы дополнительные данные. Введите высоту: '))
                v = self.areas[0] * h / 3
                print(f'Объем {self.name}a равен {v}')  # type: float
                return v
            if self.name == key:
                if key == 'цилиндр' or key == 'конус':
                    v_base = value[1] * self.radius[0] ** 2 * self.h[0]  # type: float
                    if key == 'цилиндр':
                        print(f'Объем {self.name}a равен {v_base}')
                        return v_base
                    if key == 'конус':
                        v = v_base / 3
                        print(f'Объем {self.name}a равен {v}')  # type: float
                        return v
            if self.name == key and key == 'шар':
                v = (4 * value[1] * self.radius[0] ** 3) / 3
                print(f'Объем {self.name}a равен {v}')  # type: float
                return v

    ''' метод расчета окружности '''

    @classmethod
    def circumference(cls):
        radius = float(input((' Введите радиус окружности: ')))  # type: float
        pi = 3.14   # type: float
        l = 2 * pi * radius  # type: float
        print(f'Длина окружности равна {l}')
        return l


'''Словари с необходимыми данными для расчетов.'''

name_flat_figures = {1: 'квадрат',  2: 'прямоугольник', 3: 'треугольник',
                     4: 'трапеция', 5: 'ромб',          6: 'круг'}

name_volumetric_figures = {1: 'куб',     2: 'параллелепипед', 3: 'пирамида',
                           4: 'цилиндр', 5: 'конус',          6: 'шар'}


''' Функция с циклом. Выбор данных для плоских фигур. '''
def while_for_flat():
    while True:
        name = int(input(' 1 - квадрат, 2 - прямоугольник, 3 - треугольник, '
                         '4 - трапеция, 5 - ромб, 6 - круг, 7 - Назад, 8 - Выход --> '))
        while True:
            for key, value in name_flat_figures.items():
                if name == key:
                    figures = FlatFigures(value)
                    if name != 6:
                        question_2 = int(input(' 1 - Площадь, 2 - Периметр, 3 - Назад, 4 - Выход -->  '))
                        if question_2 == 1:
                            figures.input_sides()  # метод класса для пользовательского ввода
                            figures.area()  # метод класса для расчетной области
                            continue
                        if question_2 == 2:
                            figures.input_sides()
                            figures.perimeter()  # метод класса для расчета объема
                            continue
                        if question_2 == 3:
                            return while_for_flat()  #вернуться, чтобы выбрать цифры
                        if question_2 == 4:
                            return main_py()  # выход
                    if name == 6:
                        question_2 = int(input(' 1 - Площадь, 2 - Периметр, 3 - Диаметр, 4 - Назад, 5 - Выход -->  '))
                        if question_2 == 1:
                            figures.input_sides()  # метод класса для пользовательского ввода
                            figures.area()  # метод класса для расчетной области
                            continue
                        if question_2 == 2:
                            figures.input_sides()
                            figures.perimeter()  # метод класса для расчета объема
                            continue
                        if question_2 == 3:
                            FlatFigures.diameter()  # метод класса для расчета диаметра
                            continue
                        if question_2 == 4:
                            return while_for_flat()  # вернуться, чтобы выбрать цифры
                        if question_2 == 5:
                            return main_py()  # выход
                if name == 7:
                    main_py()  # вернуться, чтобы выбрать фигуры класса
                if name == 8:
                    return main_py()  # выход


''' Функция с циклом. Подбор данных для объемных фигур.'''


def while_for_volume():
    while True:
        name = int(input(' 1 - куб, 2 - параллелепипед, 3 - пирамида, 4 - цилиндр, 5 - конус, 6 - шар, 7 - Назад, 8 - Выход -->  '))
        while True:
            for key, value in name_volumetric_figures.items():
                if name == key:
                    figures_v = VolumetricFigures(value)
                    if name == 1 or name == 2 or name == 3:
                        question_2 = int(
                            input(' 1 - Площадь, 2 - Объем, 3 - Назад, 4 - Выход -->  '))
                        if question_2 == 1:
                            figures_v.input_sides()  # метод класса для пользовательского ввода
                            figures_v.area()  # метод класса для расчетной области
                            continue
                        if question_2 == 2:
                            figures_v.input_sides()
                            figures_v.volume()  # метод класса для расчета объема
                            continue
                        if question_2 == 3:
                            return while_for_volume()  # return to choose figures
                        if question_2 == 4:
                            return main_py()  # exit
                    if name == 4 or name == 5 or name == 6:
                        question_2 = int(input(' 1 - Площадь, 2 - Объем, 3 - Диаметр окружности, 4 - Длина окружности, 5 - Назад, 6 - Выход -->  '))
                        if question_2 == 1:
                            figures_v.input_sides()  # метод класса для пользовательского ввода
                            figures_v.area()  # метод класса для расчетной области
                            continue
                        if question_2 == 2:
                            figures_v.input_sides()
                            figures_v.volume()  # метод класса для расчета объема
                            continue
                        if question_2 == 3:
                            VolumetricFigures.diameter()  # метод класса для расчета диаметра
                            continue
                        if question_2 == 4:
                            VolumetricFigures.circumference()  # метод класса для вычисления окружности
                            continue
                        if question_2 == 5:
                            return while_for_volume()  # вернуться, чтобы выбрать цифры
                        if question_2 == 6:
                            return main_py() # выход
                if name == 7:
                    main_py()  # вернуться, чтобы выбрать фигуры класса
                if name == 8:
                    return main_py()  # выход



''' Консольная программа.'''


def main_py():
    question = int(input('----------------------------------------------\n '
                         '1 - Плоские фигуры, 2 - Объемные фигуры -->  '))
    if question == 1:
        while_for_flat()
    if question == 2:
        while_for_volume()


main_py()