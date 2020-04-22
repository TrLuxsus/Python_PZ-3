# Індівідуальне завдання варіант 9

# Класс Равнобедренный треугольник
# Свойства: основание и боковая сторона
# Операции: увеличение/уменьшение размера на определенный процент;
# вычисление длины медианы, принадлежащей любой стороне;
# вычисление периметра и площади;
# определение значений углов.

import math

class EquilateralTriangle:
    __base = 0
    __side = 0


    # Геттер основания
    def get_base(self):
        return self.__base

    # Сеттер основания
    def set_base(self, base):
        try:
            int(base)
        except ValueError:
            print("Сторона должна быть числом")
            return False
        base = int(base)
        if base <= 0:
            print("Сторона должна быть больше 0")
            return False
        if self.__side == 0:
            self.__base = base
        elif base > self.__side * 2:
            print("Не выполняется неравенство треугольника")
            return False
        else:
            self.__base = base

    # Геттер бедра
    def get_side(self):
        return self.__side

    # Сеттер бедра
    def set_side(self, side):
        try:
            int(side)
        except ValueError:
            print("Сторона должна быть числом")
            return False
        side = int(side)
        if side <= 0:
            print("Сторона должна быть больше 0")
            return False
        if self.__base == 0:
            self.__side = side
        elif self.__base > side * 2:
            print("Не выполняется неравенство треугольника")
            return False
        else:
            self.__side = side

    # Увеличение размера на процент
    def increase(self, percent):
        if percent <= 0:
            print("Процент должен быть больше 0")
            return False
        else:
            self.__base += self.__base * percent / 100
            self.__side += self.__side * percent / 100

    # Уменьшение размера на процент
    def reduce(self, percent):
        if 0 <= percent == 100:
            print("Процент должен быть больше 0 и меньше 100")
            return False
        else:
            self.__base -= self.__base * percent / 100
            self.__side -= self.__side * percent / 100
