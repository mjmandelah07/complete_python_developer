print(bin(5))  # changing to binary number
print(int("0b101", 2))  # converting back to base two

# variables stores information to be used in the program
snake_case = 190
_my_age = 25
my_NAME = "Mojisola Aramide"
div = snake_case / _my_age
a, b, c = 5, 6, 4

print("My name is", my_NAME + ", and im", _my_age, "years old.", "And i have", snake_case, "naira")
print(type(div))
print("I have", a, "pencils and", c, "pens.", "And my dad has", b, "houses")

# constants variable are not to be changed
PI = 3.14
print(PI)

# dunder are with two underscore
# __build_class_()

# augmented assignment operators
some_value = 8
some_value += 3
some_value -= 2

print(some_value)

# string concatenation
print("hello", 5)

#  casting
print(type(int(str(100))))

# OR
a = str(100)
b = int(a)
c = type(b)

print(c)

# escape sequences
physics = 'Physics is natural \'nature\' science that involve \t the study of matter and its motion \n through space'

print(physics)

# formatted strings
name = "Johnny"
age = 54

print(f"Hi i'm {name}. And im {age} years old")

# OR
name = "Johnny"
age = 54
txt = 'Hi i\'m {}. \nAnd im {} years old'

print(txt.format(name, age))

# Or
print("Hi i'm {fname}. And im {age} years old".format(fname="John", age=54))

# string indexes
arc = "architecture"

# [start:stop:stepover]
print(arc[0:11:2])
print(arc[2:])
print(arc[:12])
print(arc[::2])
print(arc[-1])
# to reverse
print(arc[::-1])

# immutability - strings cant be changed
selfish = '01234567'

selfish += '8'

print(selfish)

# len()
greet = 'Hello dear'

print(greet[0:10])
print(greet[0:len(greet)])

# string methods
quote = "to be or not to be"

print(quote.upper())
print(quote.capitalize())
print(quote.find("or"))
print(quote.replace("be", "me"))

# LIST
# LIST SLICING
amazon_cart = ['laptop', 'earring', 'shoe', 'hair']

amazon_cart[1] = 'sneakers'
new_cart = amazon_cart[:]
new_cart[3] = 'bag'

print(amazon_cart)
print(new_cart)

# MATRIX
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])

# list methods
basket = [1, 2, 3, 4, 5]
basket.append(6)
new_list = basket[:]
new_list.insert(5, 8)

print(basket)
print(new_list)

#  list methods 2
basket = ["a", "f", "r", "b", "c,", "y"]
basket.sort()

new_basket = basket

print(basket)

print(new_basket[::-1])

# How to generate a number list
ran_ge = list(range(30))

print(ran_ge)

# .join()

name = "-".join(["Hi", "my", "name", "is", "grace"])
print(name)

# list unpacking
un_packing = list(range(20))
a, b, c, *others, d = un_packing

print("The length of unpacking is: ", len(un_packing))
print(a)
print(b)
print(c)
print(others)
print(d)

# DICTIONARIES
dict_1 = {
    "a": [1, 2, 3],
    "b": "Hello",
    "c": True
}
my_list = [{
    "a": [1, 2, 3],
    "b": "Hello",
    "c": True}, {

    "a": [1, 2, 3],
    "b": "Hello",
    "c": True}]

print(my_list[0]["a"][2])
print(dict_1["a"][1])
# new dic
dict_2 = {
    "a": [1, 2, 3],
    "b": "Hello",
    "c": True,
    "age": 43
}
dict_3 = dict_2.copy()
dict_3["d"] = False
x = dict_2.update({"age": 55})

print(dict_2.keys())
print(dict_2.items())
print(dict_2.values())
print(dict_3)
print(dict_2)
print("age" in dict_3)

# Tuple, can not be modified, cannot be sorted or reversed
# tuple is fasted than list
# used for latitude or longitude
my_tuple = (1, 2, 3, 4, 5, 5, 5)
x, y, z = (1, 2, 3)
a, b, c, *other = (1, 2, 3, 4, 5)

print(other)
print(x, y, z)
print(my_tuple.count(5))
print(my_tuple.index(5))
print(len(my_tuple))

# Set : are unordered collection of unique objects
# set: accepts no duplicates
# set does not accept index
my_set = {1, 2, 3, 4, 5, 6, 7, 8}
my_list = [1, 2, 3, 4, 5, 5, 6, 6]
my_set2 = set(my_list)
my_set3 = {1, 2, 3, 4, 5, 5, 6, 6}
my_set4 = my_set2.copy()
my_set5 = {4, 5, 6, 7, 8, 9}
print(my_set2)
print(5 in my_set2)
print(len(my_set3))
print(my_set4)

print(my_set4.difference(my_set5))
my_set.discard(6)
print(my_set)
print(my_set.intersection(my_set5))
print(my_set.isdisjoint(my_set5))  # false result cause the have something in common
print(my_set | my_set5)
print(my_set.issubset(my_set5))
print(my_set.issuperset(my_set5))
my_set5.difference_update(my_set)
print(my_set5)  # 6 has been discarded from my_set
