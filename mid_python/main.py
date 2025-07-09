def returnFn():
    def printSome():
        print("this is the child fn")

    return printSome


def calc(num):
    def check(x):
        return x**num

    return check


result = calc(3)(2)
print(result)
