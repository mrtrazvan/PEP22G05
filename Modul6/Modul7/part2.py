from  datetime import datetime,timedelta

# clasa car are 2 atribute , serial , si date_sold

class Car:
    def __init__(self,serial,date_sold):
        self.serial = serial
        self.date_sold= date_sold
        self.warranty_expiration= date_sold +timedelta(days=365)

    # def __iter__(self):
    #     return self

    # def __next__(self):

# metodele iter si next

# clasa shop unde se adauga masinile intr o lista


class Shop:
    def __init__(self):
        self.cars = []

    def sell_car(self,serial, date_sold):
        new_car = Car(serial,date_sold)
        self.cars.append(new_car)

    # ne returneaza masinile cu garantina expirata
    def expired_warranty(self,name,date):
        expired_warranty_cars=[]
        for car in self.cars:
            if car.warranty_expiration <date:
                expired_warranty_cars.append(car)
            return expired_warranty_cars

my_shop = Shop()

my_shop.sell_car(1588,datetime(2019,1,20,10,30,32))
my_shop.sell_car(1692,datetime(2021,1,20,9,20,25))
my_shop.sell_car(1994,datetime(2022,1,20,9,10,50))

expired_warranty = my_shop.return_expired_warranties(datetime.now())

print(expired_warranty)
