import datetime


class Magazin:
    def __init__(self):
        self.cars = []

    def add_car(self, serial:int , production_date:datetime):
        self.cars.append((serial,production_date))

    def covered_cars(self):
        covered_cars=[]
        current_date = datetime.now()
        for serial in production_date = production_date+ timedelta(days= 3*365)
            if warranty_expiration_date>current_date:
                covered_cars.append((serial,warranty_expiration_date-current_date))
            return covered_cars

    def warranty_expired(self):
        covered_cars = self.covered_cars()
        for serial ,remaining_time in covered_cars:
            if remaining_time.days <= 0:
                print(f"Car with serial{serial}is not covered by warranty")

magazin = Magazin()

magazin.add_car(1588,datetime(2019,1,20,10,30,32))
magazin.add_car(1692,datetime(2021,1,20,9,20,25))
magazin.add_car(1994,datetime(2022,1,20,9,10,50))

magazin.warranty_expired()

for serial, remaining_time in magazin.covered_cars():
    print(f"Car with serial{serial} has {remaining_time.days}left on its warranty")




