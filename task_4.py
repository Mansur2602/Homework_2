class MainClass:
    def __init__(self, text):
        self.text = text

    def set_text(self, text=''):
        if text:
            self.text = text


class SubClass(MainClass):
    def __init__(self, text, number):
        super().__init__(text)
        self.number = number



main_obj = SubClass("Hello", 5)
print(main_obj.text)  
print(main_obj.number) 
main_obj.set_text("World")
print(main_obj.text)  
