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


# create a function to calculate the highest even
def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)


print("The highest even in the list[11, 10, 21, 12, 54, 23] is: ", highest_even([11, 10, 21, 12, 54, 23]))

