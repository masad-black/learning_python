# Q1: age categorixation

# user_age = input("Hey enter you age???")
# user_age = int(user_age)

# if user_age < 13:
#     print("You are a child!!!")
# elif user_age >=13 and user_age <= 19:
#     print("You are a teenager!!!")
# elif user_age >=20 and user_age < 59:
#     print("You are a adult!!!")
# elif user_age >59:
#     print("You are senior citizen of our society:))")

# Q2: movies ticket price

# user_age = 10
# curr_day = "tuesday"

# if user_age < 18:
#     print("Your tikcet price is $8")
# elif user_age >= 18:
#     print("Your ticket price is $12")
    
# if curr_day == "wednesday":
#     print("Your ticket price is $8 and you got $2 discout")

# Q3: password checker

# 1 upper and lower case letter
# atleast one special case char

password = "Hey123$$$ "
upper_case = False
lower_case = False
special_cahr = False

for char in password:
    if char.isupper():
        upper_case = True
    elif char.islower():
        lower_case = True
    elif char in "!@#$%^&*()":
        special_cahr = True

main_con = upper_case and lower_case and special_cahr


if len(password) < 6 and main_con: 
    print("You password is too weak!!!!")
elif len(password) < 10 and main_con: 
    print("You password is medium!!!!")
elif len(password) > 10 and main_con: 
    print("You password is strong!!!!")
else:
    print("Your password is not acceptable!!!")
        