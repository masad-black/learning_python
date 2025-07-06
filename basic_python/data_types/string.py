"""
Python string

"""

# both are the same string
my_str = "$#.....hello this is the basic! string....!@"
obj_str = str("Hello this is the object string")

# print(type(my_str), type(obj_str))
# print(my_str, obj_str)

# Methods of the string

print(f"before change: {my_str}")
print()


print("first char upper case: ", my_str.capitalize())
print("count the occurance: ", my_str.count("llo"))
print("if string end with the specific str: ", my_str.endswith("g"))
print("if string start with the specific str: ", my_str.startswith(("he", "hello")))
print("find the position of sub in string: ",  my_str.find("00"))
print("need to check if the sub is in the string: ", "llo" in my_str)
print("find the index of sub in string: ",  my_str.index("he"))
print("joining the string: ", "___".join(["light", "goku", "eren", "toji"]))
print("converting the str into lowercase: ", my_str.lower())
print("converting the str into uppercase: ", my_str.upper())
print("replcaing string: ", my_str.replace("basic", "Mega Tron"))
print("converting string into the list: ", my_str.split("!"))
print("removing the chars from start and end: ", my_str.strip("$#.!@"))
print("first char upper and other are lower: ", my_str.title())
print("getting a sub string from the string: ", my_str[-5:-1])




print()
print(f"after change: {my_str}")

