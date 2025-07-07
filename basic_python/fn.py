import math

def printSomething(message):
    print("inside the fn")
    print(message)

def giveInfoAboutCircle(radius):
    area_of_circle = math.pi * (radius ** 2)
    circumfarance_of_circle = 2 * (math.pi * radius) 

    return {
       "area":  area_of_circle,
        "cir": circumfarance_of_circle
    }

    # * we can also do this, but then there should be no key
    #     return {
    #      area_of_circle,
    #      circumfarance_of_circle
    # }

# setting default values in the fn
def greetUser(name = "Please enter some name"):
    print(f"Hello, {name} !!!")

# handelling multipul parameter in the fn
def sum_all_num(*args):
    # * args is a tupple
    # * *args is whole values

    # print(type(args))
    # print(type(*args))
    return sum(args)

# handelling mulltipul parameters
def handleParameters(**kwargs):
    # this will give use the dict
    # print(kwargs)
    # print(kwargs.keys())
    # print(kwargs.values())
    # print(kwargs.items())

    for (key, val) in kwargs.items():
        print(f"You name is {val} and age is {val} and role is {val}")


def f(a, L=[]):
    print(a)
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))




# handleParameters(name="Asad", age=20)
# handleParameters("Asad", 30)
# handleParameters(age=20,name= "asad")
# handleParameters(name="Asad", age=20, role="backend")

    
# print(sum_all_num(1,2,3,4))


# greetUser("Toji Zennin")
# greetUser("now")



# data =  giveInfoAboutCircle(10)
# print(data["area"], data["circumfarance"])
# print(data)


# printSomething("I am learning about the fn's in the python!!!!")