# no3
is_magician = True
is_expert = False
# check if magician and expert: "you are a master magician"
if is_magician and is_expert:
    print("you are a master magician")

# check if magician but not expert: "at least you're getting there"
elif is_magician and not is_expert:
    print("at least you're getting there")

# check if not a magician: "you need magic powers"
elif not is_magician:
    print("You need magic powers")

# No4 loop the list and add it up
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sum_up = 0
for item in my_list:
    sum_up += item
print(sum_up)

# find the index number of 50 in the range
for i, char in enumerate(list(range(60))):
    if char == 50:
        print("index of 50 is: ", i)

# print the picture if == 1, print(*), if == 0 print(" ")
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]
for image in picture:
    for pixel in image:
        if pixel == 1:
            print("*", end="")
        else:
            print(" ", end="")
    print(" ")

# check for duplicates
some_list = ["a", "b", "c", "b", "d", "m", "n", "n", "n"]
duplicates = []
for value in some_list:
    if some_list.count(value) > 2:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)

# NO1 - Write a program that takes input of your birth year and output your age
birth_year = input('Enter your birth year: ')
name = input("Enter your firstname: ")
age = 2021 - int(birth_year)

print(f"{name.capitalize()}, You are {age} years old.")

# NO2 - OUTPUT A PASSWORD AND USERNAME
user_name = input("Enter your username: ")
pass_word = input("Enter your password: ")

password_hidden = "*" * len(pass_word)

print(f"Hi {user_name}, your password {password_hidden}, is {len(pass_word)} letter long")
