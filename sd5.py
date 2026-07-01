class vachal:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display_info(self):
        print(f" brand:{self.brand},model:{self.model}")
class car(vachal):
    def __init__(self,brand,model,seats):
        super().__init__(brand,model)
        self.seats=seats
    def display_info(self):
        super().display_info()
        print(f"seats:{self.seats}")
class bike(vachal):
    def __init__(self,brand,model,engine):
        super().__init__(brand,model)
        self.engine=engine
    def display_info(self):
        super().display_info()
        print(f" engine cc:{self.engine}")
o=bike("saurabh","s7",7)
o.display_info()
