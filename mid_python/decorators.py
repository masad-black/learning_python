"""
decorator are like keyword, that is used to increase the existing functionallity of some other functions

there are many decorators each have their own purpose and need

"""


def val(*args, **kwargs):
    print(type(args))
    print(" ".join(str(arg) for arg in args))


val("asad", "asda", 1, True, False, None, model="Honda")


# @staticmethod: is used to make class fn's static

# @property: makes the class attribute read only
