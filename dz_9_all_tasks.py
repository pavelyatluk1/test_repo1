# Pavlo Yatluk
# #1  dz_9_1 Клас автомобіля.

class Car(object):
    def __init__(self, brand, color, v_engine):
        self.brand = brand
        self.color = color
        self.v_engine = v_engine

    def direct_drive_1(self):
        return "Їхати вперед"

    def direct_drive_2(self):
        return "Їхати назад"


mycar = Car('Opel', "Red", 1.6)

print(mycar.color)
print(direct_drive_1())

# Клас
# автомобіля
# Car2


class Car2(Car):

    def direction_drive_3(self):
        return "повертати праворуч"

    def direction_drive_4(self):
        return "повертати ліворуч"


print(direction_drive(self))

# #2. Класи TexProcessor, TextLoader, DataInterface







#3. Клас Палалелограм з аргументами wigth та lenght і методом get_area.

class Parallelegram():
    def __init__(self, width, lenth):
        self.width = width
        self.lenth = lenth

    def get_area(self):
        return self.lenth * self.width

pl = Parallelegram(10, 15)

print(pl.get_area())


# Клас Квадрат
class Square(Parallelegram):

    def get_area(self):
        return self.width ** 2
sq = Square(10, 10)
print(pl.get_area())


