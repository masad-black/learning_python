import math
import random

""" 
python support 3 data types in number

1: integer int()
2: float float()
3: complex complex()

"""

int_num = 10
float_num = 19.34

# print(int_num, float_num)

val = "0"
boolean = False

# converting different values
# print(float(boolean))

# practicing most commonly used math fn's

# ceil method will move the number up
# print(math.ceil(3.00001))

# floor method will move the number down
# print(math.floor(4.999999))

# give the power
# print(math.pow(2, 5)) this will give us float
# print(2 ** 5) # this will give us int

# print(math.pi, math.e)

# print(math.isfinite(10))
# print(math.isinf(10))


# print(int_num + float_num)
# print(int_num * float_num)
# print(int_num / float_num)
# print(int_num % float_num)
# print(int_num ** float_num)

new_array = ["asad", "haider", "ahmed", "amna"]

print("gen random no: ", random.random())
print("gen random int no: ", random.randint(1, 10))
print("selecting one form the list: ", random.choice(new_array))
print("gen random float no: ", random.uniform(1, 10))

print("before ", new_array)

print("shuffling the list: ", random.shuffle(new_array))

print("after", new_array)






