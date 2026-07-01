from abc import ABC,abstractmethod
class employe(ABC):
    def __init__(self,name):
        self.name=name
    
    def calculate_salary(self):
        pass
class intern(employe):
    def __init__(self,name,stipend):
        super().__init__(name)
        self.stipend=stipend
    def calculate_salary(self):
        return self.stipend
class full(employe):
    def __init__(self,name,m_salary):
        super().__init__(name)
        self.m_salary=m_salary
    def calculate_salary(self):
        return self.m_salary
class con(employe):
    def __init__(self,name,hour_rate,hour_worked):
        super().__init__(name)
        self.hour_rate=hour_rate
        self.hour_worked=hour_worked
    def calculate_salary(self):
        return self.hour_rate*self.hour_worked
i = intern("Saurabh", 5000)
f = full("Kumar", 30000)
c = con("Raj", 200, 120)

print("Intern Salary:", i.calculate_salary())
print("FullTimeEmployee Salary:", f.calculate_salary())
print("ContractEmployee Salary:", c.calculate_salary())



    