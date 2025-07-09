"""
in python we can handle exception that can occur, just like js, they have trycatch statmetn
there are different types of excetions

1: NameError
2: FileNotFoundError
3: ValueError


"""

# try:
#     num = int(input("Enter the number!!! \n"))
#     print(num, nigga)
# except ValueError:
#     print("Oops something is wrong!!!")
# except NameError:
#     print("undefined vairable is suing!!!")


# try:
#     f = open("context.txt")
#     print(f)
# except FileNotFoundError as e:
#     # print(
#     #     f"Sorry, file not found!! args: {e.args}, no: {e.errno}, name: {e.filename}, name2: {e.filename2}, str: {e.strerror}"
#     # )
#     print(e)


# try:
#     # raise Exception("Hello this is custome exectiion")
#     print("Hello")
# except Exception as e:
#     print("Errro: ", e)
# finally:
#     print("this will be executed!!!, any ways")


try:
    raise NameError("name is not correct")
except NameError as e:
    print("error!!", e)
