# create a class called SuperList and allow us access through index using dunder methods
class SuperList(tuple):
    def __len__(self):
        return 100


super_list = SuperList()
print(len(super_list))
this_tuple = list(super_list)
this_tuple.append(7)
print(this_tuple[0])


# list
class SuperList(list):
    def __len__(self):
        return 50


super_list = SuperList()
print(len(super_list))
super_list.append(6)
print(super_list[0])
print(issubclass(SuperList, list))  # is SuperList subclass of list = True
print(issubclass(list, object))


# set
class SuperList(set):
    def __len__(self):
        return 80


super_list = SuperList()
print(len(super_list))
this_set = len(super_list)

# use lambda to square the list
my_list = [5, 4, 3, 2, 1]

print(list(map(lambda item: item ** 2, my_list)))

# list sorting
# sort according using the second value in the tuple
a = [(0, 2), (4, 3), (9, 9), (10, -1)]

a.sort(key=lambda x: x[1])
print(a)

# list sorting
# sort according using the third value in the tuple
a = [(0, 2, 5), (4, 3, 6), (9, 9, -2), (10, -1, -3)]

a.sort(key=lambda x: x[2])
print(a)

# comprehension
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
