class Stadium:
    def __init__(self, name,date,country,city,capacity):
        self.__name = name
        self.date = date
        self.country = country
        self.city = city
        self.capacity = capacity
    def get_name(self):
        return self.__name
    def print_info(self):
        print(self.get_name(), self.date,self.country,self.city,self.capacity)

a = Stadium(input("Введите название: "), input("Введите дату открытия: "), input("Введите страну: "), input("Введите город: "), input("Введите вместимость: "))
print(a.print_info())