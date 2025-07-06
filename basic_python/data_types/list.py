"""
In python list can be build with many different ways

1: using squar brackets []
2: using list comprehension [x for x in range(10)]
3: using the constructor list()

"""

my_list = ["eren", "toji", "goku"]
obj_list = list([1,2,3,4,5,6,7])

# this is the memory refrence we are giving no the list itself
copy_list = my_list

# both are samex
# print(type(my_list), type(obj_list))

print("before: ", my_list, copy_list)
print()


print("toji"  in my_list)
print("sakura" not in my_list)
print("concatinatio: ",  my_list + obj_list)
print("accessing the element in the list with the idx: ", my_list[0], my_list[2], my_list[len(my_list) -1])
print("slicing the list: ", my_list[0: 2])
print("length of the list: ", len(my_list))
print("min and max: ", min(my_list), max(my_list))
print("min and max: ", min(obj_list), max(obj_list))
print("index of specific ele in the  list: ", my_list.index("eren"))
print("count occurences: ", my_list.count("eren"))

# now in this we are giving another refrence no the same refrence of (my_list)
shallow_copy = my_list.copy()

# replacing the ele in the list
my_list[0] = "mikasa"

# adding new item at the end of the list
my_list.append("main hero!!!")

# removing all ele from the list
# my_list.clear()

# inserting ele at specific index
my_list.insert(0, "Mega tron!!!")

# remove element at the end of the list
print(my_list.pop())

# reverse the list
print(obj_list.reverse())

# removing the ele 
print(my_list.remove("toji"))

copy_list.append("change is the main one!!")

print()
print("after: ", my_list, copy_list)