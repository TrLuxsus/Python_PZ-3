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

    # Медиана к основанию
    def median_to_base(self):
        if self.__side == 0 or self.__base == 0:
            print("Задайте все стороны")
            return False
        else:
            return round(((math.sqrt(4*pow(self.__side, 2) - 2*pow(self.__base, 2))) / 2), 2)

    # Медиана к бедру
    def median_to_side(self):
        if self.__side == 0 or self.__base == 0:
            print("Задайте все стороны")
            return False
        else:
            return round(((math.sqrt(2 * pow(self.__base, 2))) / 2), 2)

    # Периметр
    def perimeter(self):
        if self.__side == 0 or self.__base == 0:
            print("Задайте все стороны")
            return False
        else:
            return self.__base + self.__side * 2

    # Площадь
    def area(self):
        if self.__side == 0 or self.__base == 0:
            print("Задайте все стороны")
            return False
        else:
            return round(self.__base * self.median_to_base() / 2, 2)
        
    # Углы при основании
    def angle_base(self):
        if self.__side == 0 or self.__base == 0:
            print("Задайте все стороны")
            return False
        else:
            return round(math.acos(self.__base / self.__side / 2) * 180 / math.pi, 2)

    # Угол при вершине
    def angle_top(self):
        if self.__side == 0 or self.__base == 0:
            print("Задайте все стороны")
            return False
        else:
            return round(180 - 2 * self.angle_base(), 2)


def main():
    triangle = EquilateralTriangle()
    print("Основание при инициализации: ", triangle.get_base())
    print("Бедро при инициализации: ", triangle.get_side())

    # Попытка установки некоректных значений
    triangle.set_base("три")
    triangle.set_side("четыре")
    triangle.set_base(-2)
    triangle.set_side(0)

    # Проверка неравенства треугольника
    triangle.set_base(5)
    triangle.set_side(1)

    # Проверка вазова методов на треугольнике с неопределенными сторонами
    triangle.perimeter()
    triangle.angle_base()
    triangle.median_to_base()

    # Проверка вазова методов на полностью заданом реугольнике
    triangle.set_side(10)
    print("Тетсовый треугольник основание: ", triangle.get_base())
    print("Тетсовый треугольник бедро: ", triangle.get_side())

    # Попытка удаления через уменьшение сторон до 0
    triangle.reduce(100)

    print("До изменений размера основание: ", triangle.get_base())
    print("До изменений размера бедро: ", triangle.get_side())

    print("Уменьшаем в 2 раза")
    triangle.reduce(0)
    triangle.reduce(50)

    print("Размер основания: ", triangle.get_base())
    print("Размер бедра: ", triangle.get_side())

    print("Увеличиваем в 3 раза")
    triangle.increase(-200)
    triangle.increase(200)

    print("После изменеий размера основание: ", triangle.get_base())
    print("После изменеий размера бедро: ", triangle.get_side())

    print("Периметр: ", triangle.perimeter())
    print("Площадь: ", triangle.area())
    print("Медиана к основанию: ", triangle.median_to_base())
    print("Медиана к бедру: ", triangle.median_to_side())
    print("Углы при основании: ", triangle.angle_base())
    print("Угол при вершине: ", triangle.angle_top())


if __name__ == '__main__':
    main()
