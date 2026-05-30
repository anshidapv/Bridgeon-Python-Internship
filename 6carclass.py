class car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer=0
    def drive(self,km):
        if km > 0:
            self.odometer += km
    def get_info(self):
        return f"{self.year} {self.model} , mileage:{self.odometer}km"
car =car("toyota","corolla",2022)
car.drive(150)
print(car.get_info())