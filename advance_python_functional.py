# pure function
def multiply_by3(li):
    new_list = []
    for item in li:
        new_list.append(item * 3)
    return new_list


print(multiply_by3([1, 2, 3]))


# map can also be used to change username to capital in a list
# map - gives back the same output
def multiply_by3(items):
    return items * 3


print(map(multiply_by3, [1, 2, 3]))
print(list(map(multiply_by3, [1, 2, 3])))

# or
my_list = [2, 3, 4, 5]


def multiply_by2(it):
    return it * 2


print(map(multiply_by2, my_list))
print(list(map(multiply_by2, my_list)))
print(my_list)

# or set
my_set = {2, 3, 4, 5}


def multiply_by2(j):
    return j * 2


print(map(multiply_by2, my_set))
print(set(map(multiply_by2, my_set)))

# filter - sometimes give back less than we give
# to check true or false
my_list = [2, 3, 4, 5]


def multiply_by3(li):
    return li * 3


def only_odd(area):
    return area % 2 == 1


print(map(multiply_by3, my_list))
print("This is a result for using the map function by multiplying the list by 3: ", list(map(multiply_by3, my_list)))
print("This is a result for using the filter function: ", list(filter(only_odd, my_list)))
print("This is the list: ", my_list)

# zip
my_list = [2, 3, 4, 5]
your_list = [20, 30, 40, 50]
their_list = ("yemi", "gbenga", "seun", "dupe")


def multiply_by3(its):
    return its * 3


def only_odd(i):
    return i % 2 == 1


print(map(multiply_by3, my_list))
print("This is a result for using the map function by multiplying the list by 3: ", list(map(multiply_by3, my_list)))
print("This is a result for using the filter function: ", list(filter(only_odd, my_list)))
print("This is a result for using the zip function: ", list(zip(my_list, your_list)))
print("This is a result for using the zip function: ", list(zip(my_list, your_list, their_list)))
print("This is the list: ", my_list)

# reduce
# import functools for functions
import functools as ft

my_list = [2, 3, 4, 5]
your_list = [20, 30, 40, 50]
their_list = ("yemi", "gbenga", "seun", "dupe")


def multiply_by2(z):
    return z * 2


def only_odd(itz):
    return itz % 2 == 1


def accumulator(acc, ab):
    print(acc, ab)
    return acc * ab


print(map(multiply_by2, my_list))
print("This is a result for using the map function by multiplying the list by 2: ", list(map(multiply_by2, my_list)))
print("This is a result for using the filter function: ", list(filter(only_odd, my_list)))
print("This is a result for using the zip function: ", list(zip(my_list, your_list)))
print("This is a result for using the zip function: ", list(zip(my_list, your_list, their_list)))
print("Using the reduce function, setting the accumulator to default 1: ", ft.reduce(accumulator, my_list, 1))
print("This is the list: ", my_list)
print('\n')

# lambda expressions
# functions u only use once
# no need to have names
# lambda param: action(param), data
import functools as ft
import operator as op

my_list = [2, 3, 4, 5]
our_name = ["Moji", "Dorcas", "Yemi", "Seun"]

print(list(map(lambda u: u * 3, my_list)))
print(list(filter(lambda v: v % 2 != 0, my_list)))
print(ft.reduce(lambda c, b: op.add(c, b), my_list, 1))
print(ft.reduce(lambda acc, hit: acc + hit, my_list, 2))
print(list(zip(my_list, our_name)))

# # use lambda to square the list
my_list = [5, 4, 3, 2, 1]

print(list(map(lambda k: k ** 2, my_list)))

# list sorting
# sort according using the second value in the tuple
a = [(0, 2), (4, 3), (9, 9), (10, -1)]

a.sort(key=lambda xx: xx[1])
print(a)

# list sorting
# sort according using the second value in the tuple
a = [(0, 2, 5), (4, 3, 6), (9, 9, -2), (10, -1, -3)]

a.sort(key=lambda xxx: xxx[2])
print(a)

# list comprehensions
# make a list for hello
my_list = []

for item in "Hello":
    my_list.append(item)

print(my_list)

# or list comprehension
my_list = [item for item in "hello"]
print(my_list)

# make a list for the range of 100
my_list2 = []

for x in range(0, 20):
    my_list2.append(x)

print(my_list2)

# or
my_list2 = [x for x in range(15)]

print(my_list2)

# multiply the output with 2
my_list3 = []

for x in range(0, 15):
    my_list3.append(x ** 2)

print(my_list3)

# or
my_list3 = [x ** 2 for x in range(0, 15)]

print(my_list3)

# print out the even number in the list
my_list4 = []

for y in range(0, 15):
    if y % 2 == 0:
        my_list4.append(y ** 2)

print(my_list4)

# or
my_list4 = [y ** 2 for y in range(0, 15) if y % 2 == 0]

print(my_list4)

# dictionary comprehension
simple_dict = {
    "a": 3,
    "b": 4
}
my_dict = {k: v ** 2 for k, v in simple_dict.items()}

print(my_dict)

#  if value is even
simple_dict = {
    "a": 3,
    "b": 4
}
my_dict = {k: v ** 2 for k, v in simple_dict.items() if v % 2 == 0}

print(my_dict)

# use list [1,2,3]
my_dict2 = {num: num ** 2 for num in [1, 2, 3]}
print(my_dict2)

# exercise
some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]

duplicates = []

for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)

# or

some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]

duplicates = list(set([value for value in some_list if some_list.count(value) > 1]))

print(duplicates)
