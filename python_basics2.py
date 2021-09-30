# Conditional logic
eaten = True
rice = False

if eaten:
    print("Yes, she has eaten")
elif rice:
    print("She ate rice")
else:
    print("She has not eaten anything")

eaten = True
rice = False

if eaten and rice:
    print("Yes, she has eaten rice")
elif eaten or rice:
    print("She has either eaten rice or not ")
else:
    print("She has not eaten rice")

# Ternary operator short cut
# condition_if_ True if condition else condition_if False
is_friend = False
open_door = "Open the door" if is_friend else "Don't open the door"
print(open_door)

# short circuiting
is_friend = True
is_User = True

if is_friend and is_User:
    print("Best friends")

    # loops
for item in "Zero to Mastery":
    print(item)

for item in [1, 2, 3, 4, 5]:
    print(item)

for item in {1, 2, 3, 4, 5}:
    for x in ["a", "b", "c"]:  # only when it is done here it will go back to line 42
        print(item, x)

# loop through a dictionary
user = {
    "name": "Mojisola",
    "age": 25,
    "can_swim": False
}
for item in user.items():  # will get the items both values and keys
    print(item)

for item in user.items():
    key, value = item
    print(key, value)

for key, value in user.items():
    print(key, value)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

for a, b in user.items():
    print(a, b)

# range()
for x in range(15):
    print(x)

for _ in range(5):
    print("i love geeky")

# range to make a list
for _ in range(3):
    print(tuple(range(5)))

# range to make list
for _ in range(3):
    print(set(range(5)))

# range to reverse and step over
for x in range(10, 0, -2):
    print(x)

# enumerate
for i, char in enumerate('Helloooo'):
    print(i, char)

for i, char in enumerate([1, 2, 3, 4]):
    print(i, char)

for i, char in enumerate(list(range(15))):
    if char == 10:
        print(f"index of 50 is: {i}")  # f is for format

for i, char in enumerate(set(range(5))):
    print(i, char)

# while loops
i = 0
while i < 10:
    print(i)
    break

i = 0
while i < 10:
    i += 2
    print(i)
else:
    print("Finally done looping")

i = 0
while i < len([1, 2, 3]):
    i += 1
    print(i)

my_list = [1, 2, 3]
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    break

while True:
    response = input("What is the sum of 10 and 5: ")
    if response == "15":
        print("The sum of 15 and 5 is: ", response)
        break
    else:
        print("The answer is wrong")
        break

# break, continue, pass

# functions
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]


def show_tree():
    for image in picture:
        for pixel in image:
            if pixel == 1:
                print("*", end="")
            else:
                print(" ", end="")
        print(" ")


show_tree()
show_tree()


def say_hello(name, emoji):
    print(f"Say hello {name} {emoji}")


say_hello("moji", "😂")
say_hello("Dorcas", "😍")


# parameters
# default parameters
def say_hello(name="darth", emoji="😁"):
    print(f"Hello {name} {emoji}")


say_hello("yemi", "👍")  # positional parameter

say_hello(name="seun", emoji="😉")  # keyword parameter


# return
def add(num_1, num_2):
    return num_1 + num_2


print(add(10, 5))


# function should do one thing well
# function should return something

def solution(num_1, num_2):
    return num_1 + num_2


total = solution(10, 5)
print("Total is :", total)
print("The sum of total and 10 is:", add(10, total))


# def in def
def solution(num_1, num_2):
    def another(n1, n2):
        return n1 + n2

    return another(num_1, num_2)


print(solution(10, 6))

total = solution(10, 5)

# methods vs functions
# functions
print("Hello")
print(max(1, 2, 3, 4, 5))

# methods
print("hello".capitalize())
print("hEllo".casefold())  # returns all string in lower case


# Docstrings
# allows us to comment in a function
def test(alice):
    """
     Info: This is a test function and prints parameter alice
    """

    print(alice)


test("Grace is good")
help(test)  # to search the usage
test("grace is nice".capitalize())  # capitalize only the first letter
print(test.__doc__)  # to search the usage


# find the odd and even, let the parameters be taken from users
def is_odd_or_even(num):
    if num % 2 == 0:
        print(num, "is an even number")
    else:
        if num % 2 == 1:
            print(num, "is an odd number")


number = int(input("Enter a number to check if it is an odd or even number: "))
is_odd_or_even(number)


# or
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        if num % 2 != 0:
            return False


print(f"The number being an even is: ", is_even(19))


# OR
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


print(f"The number being an even is: ", is_even(20))


# OR
def is_even(num):
    if num % 2 == 0:
        return True
    return False


print(f"The number being an even is: ", is_even(17))


# or
def is_even(num):
    return num % 2 == 0


print(f"The number being an even is: ", is_even(16))


# *args and **kwargs
# *args
def arg(*args):
    print("These are the args to be added together: ", *args)
    print("This is the tuple of the args parameter given: ", args)
    return sum(args)


print("The sum of 1, 2, 3 and 4 is: ", arg(1, 2, 3, 4))


# rules: params, *args, default parameters, **kwargs

# kwargs
def arg(*args, **kwargs):
    kwarg_total = 0
    for items in kwargs.values():
        kwarg_total += items

    print("These are the args to be added together: ", *args)
    print("This is the tuple of the args parameter given: ", args)
    return sum(args) + kwarg_total


print("So the total sum of arg function is: ", arg(1, 2, 3, 4, num1=5, num2=6))

# walrus operator ( := ) to assign or replace
a = "helloooooooo"

if (n := len(a)) > 10:
    print(f"Too long {n} elements")

# or
while (n := len(a)) > 1:
    print(n)
    a = a[:-2]

# scope - what variables o we have access to?
# global scope
total = 5


def some_func():
    total = 7
    return total


print("Total is global scope: ", total)
print("Total is local scope for some_func: ", some_func())

# dependency injection
total = 0


def count(total):
    total += 1
    return total


print(count(count(count(total))))


# non local keyword
def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner", x)

    inner()
    print("outer", x)


outer()
