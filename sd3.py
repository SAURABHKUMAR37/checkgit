class student:
    def __init__(self,name,roll_no,marks):
        self.__name=name
        self.__roll_no=roll_no 
        self.__marks=marks

    def get_name(self):
        return self.__name
    def get_roll_no(self):
        return self.__roll_no
    def get_marks(self):
        return self.__marks
    def set_name(self,name):
        self.__name=name
    def set_roll_no(self,roll_no):
        self.__roll_no=roll_no
    def set_marks(self,marks):
        self.__marks=marks
s=student("saurabh",1,230)
print(s.get_name())
print(s.get_roll_no())
print(s.get_marks())
s.set_name("mishra")
print(s.get_name())
print(s.get_roll_no())
print(s.get_marks())


