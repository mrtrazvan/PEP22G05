import time

class Car:
    color = "yellow"
    motors = ["fw-2KW engine"]
    lights = "off"
    def __int__(self,color = "red"):
        self.wheels = 4
        self.construction_date =time.time()
        self.color = color


    def start_car(self):
        print("brum...brum")
        self.lights = "on"

    @staticmethod
    def factorial(number):
        result =1
        for i in range(1,number+1):
            result *=i
        return result


    def __eq__(self, other):
        print(self.construction_date, other.construction_date)
        if self.color == other.color and self.wheels == other.wheels:
            return True
        else:
            return False


    def __str__(self):
        return "abc"



car1 = Car()
car2= Car()
print(type(car1))
print(car1.color)
time.sleep(1)

# car2 = Car()
# print(type(car2))
# print(car2.color)
# car2.color = "blue"
# print("car2 is :",car2.color)
# print("car1 is :",car1.color)
#
# car2.motors.append("rw-4KW-engine")
# print("car2 is :",car2.motors)
# print("car1 is :",car1.motors)
#
# print(id(Car))
# print(type(Car))
# print(Car.color)
# car1=Car()

# print("color befor change",car1.color)
# print(Car.__init__(car1, color="green"))
# print("color after change", car1.color)


print("lights before srat",car1.lights)
car1.start_car()
print("lights after start",car1.lights)

print("lights before srat",car1.lights)
car1.start_car()
print("lights after start",car1.lights)

print(car1.factorial(5))
print(Car.factorial(5))

print(car1 == car2)

print(car1.__str__())