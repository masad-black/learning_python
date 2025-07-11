from random import randint


class MyFirstClass:
    # we usally add the vairable here if we want all of our class to get the same data
    name = "First Class"  # this is also valid
    anime = "un changed!!!"

    #   these are like required attribute, if not given raise errro (TypeError)
    def __init__(self, name, clan):
        # in python this __init__ is like a constructor
        self.name = name
        self.clan = clan

    def printDetails(self):
        print(f"your name is: {self.name} and the clan: {self.clan}")


# Base/Main class
class Car:
    show_room_place = "Attock, Hazro!!"
    total_cars = 0

    def __init__(self, name, model, price, owner_list):
        self.name = name
        self.model = model
        self.price = price
        # this is a private attribute that is only accessable to this class, and can be accessed and modified
        # with the help of functions
        self.__owner_list = owner_list
        Car.total_cars += 1

    def printDetails(self):
        print(f"{self.name} : {self.model} : {self.price}")

    # getter fn for the private attribute
    def get_owner_list(self):
        return self.__owner_list

    def update_owner_list(self, name):
        self.__owner_list.append(name)

    # this is the static method that doesn't need object instance
    # this is also called python decorators
    @staticmethod
    def generateCarNo():
        car_plate_no = ""

        for i in range(6):
            car_plate_no += str(randint(0, 9))

        print(f"Yout car plate number is: {car_plate_no}")


# Derived class / inheritance
class ElectricCar:
    def __init__(self, name, model, price, owner_list, battery):
        # what this will do is that, super will call the upper calss/ base calss
        # and call the constructor fn and get all the variable in that
        super().__init__(name, model, price, owner_list)
        self.battery = battery

    def printMore(self):
        print(f"{self.name} : {self.model} : {self.price} : {self.battery}")

    def printDetails(self):
        print(f"{self.name} : {self.model} : {self.battery}")


car1 = ElectricCar("Ford", "Tesla", "76L", [], "67KWH")


print(isinstance(car1, MyFirstClass))
print(isinstance(car1, Car))
print(isinstance(car1, ElectricCar))


# car1 = Car("Civic", "Honda", "35L", ["honada", "supra"])
# car1.__owner_list.append("tesla")
# car1.update_owner_list("tesla")
# print(car1.get_owner_list())
# print(car1.owner_list)

# car3 = Car("HHH", "PPP", "35L", [])
# car4 = Car("GGG", "LLL", "35L", [])

# print(ElectricCar.generateCarNo())


# print(Car.total_cars)
# print(ElectricCar.total_cars)
# car1.printDetails()
# print(car1.__owner_list)

# car1.update_owner_list("Toji")
# car1.update_owner_list("Itachi")
# car1.update_owner_list("Naruto")


# print(car1.get_owner_list())


# car1.printDetails()
# car2.printDetails()
# print(car2.total_cars)

# car2.printMore()
# print(car2.show_room_place)
# print(car2.get_owner_list())


# c1 = MyFirstClass()
# print(c1.name)


# c2 = MyFirstClass("Toji ", "Zenin")
# # c2.printDetails()
# print(c2.anime)

# c2.anime = "the value is changed!!!"

# print(c2.anime)

# c3 = MyFirstClass("Itachi", "Uchia")
# # c3.printDetails()
# print(c3.anime)
