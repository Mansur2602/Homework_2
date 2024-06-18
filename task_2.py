class Book:
    def __init__(self,name,year,publisher,genre,author,price):
        self.name = name
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.__price = price
    def get_price(self):
       return self.__price
    def print_info(self):
        print(self.name,self.year,self.publisher,self.genre,self.author,self.get_price())
    
a = Book(input("Введите название: "), input("Введите год: "), input("Введите издателя: "), input("Введите жанр: "), input("Введите автора: "), input("Введите цену: "))
print(a.print_info())