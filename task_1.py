class Car:
    def __init__(self,model,year,manufacturer,engine_capacity,color,price):
        self.__model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_capacity = engine_capacity
        self.color = color
        self.price = price
    def get_model(self):
        return self.__model
    def print_info(self):
        print(self.get_model(), self.year,self.manufacturer,self.engine_capacity,self.color,self.price)

a = Car(input("Введите модель: "),input("Введите год: "), input("Введите производителя: "), input("Введите объем двигателя: "), input("Введите цвет: "), input("Введите цену: "))
print(a.print_info())