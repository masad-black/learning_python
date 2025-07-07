"""
In python there are 2 ways in which we can create the dictinonay

1: using the curlly braces {}
2: using the constructor dict()
3: and with list comphrension

"""

# with currly braces
my_dictoniary = {
    "one": "Eren",
    "two": "Toji",
    "three": "Naruto",
    "four": "Goku",
    "three": "Itachiii",
}

# with the constructor
obj_dic = dict(name="Toji", age=25, power="super human", clan="zenin")
copy_dict = obj_dic

# wiht comphrension
comp_dict = {x:x+2 for x in range(10)}

# print(my_dictoniary, obj_dic, comp_dict)

print("before")
print(obj_dic)
print()


# if we need only the key of the dictonary then
print("getting the key of list: ", list(obj_dic))

# accessing the value of dict
print("get value of dict: ", obj_dic["name"], obj_dic["clan"])

# updating the value, if the key is not present then add that key and value pair!!
print("updating the values")
obj_dic["power"] = "Killer machine!!!"

# deleting the item
print("deleting the pair")
# del copy_dict["age"]

print("name" in copy_dict)
print("jj" not in obj_dic)
print("live" in obj_dic)

print("dict items: ", obj_dic.items())

# getting the dict keys
print("keys: ", obj_dic.keys())

print("popping specific key: ", copy_dict.pop("age"))

print("getting the values: ", obj_dic.values())




print()
print("after")
print(obj_dic)
print(copy_dict)