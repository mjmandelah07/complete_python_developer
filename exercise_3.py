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

