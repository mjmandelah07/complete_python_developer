# e.g @classmethod, @staticmethod
# functions
def hello():
    print("hello geeky")
    return "Hi moji"


greet = hello
del hello  # will del hello but greet will remain

print(greet())


# use function to call function
def hello(call):
    call()
    return "done"


def greet():
    print("testing")


x = hello(greet)
print(x)


# decorator supercharge our functions
# Higher Order Function HOC - accept another function as parameter, or returns a function eg map(), filter()
def greet(func):
    func()
    pass


def greet2():
    def func():
        return 5
        pass

    return func
    pass


# decorator super charges our function, it's simple a funtion that wraps another function and enhance it or change it
def my_decorator(func):
    def wrap_func():
        print("********")
        func()
        print("-------")

    return wrap_func


@my_decorator
def hello():
    print("I'm in love with geeky")


hello()


@my_decorator
def bye():
    print("I'm done waiting for you")


bye()


def love():
    print("I cant let go of you")


love2 = my_decorator(love)
love2()

# decorator 3
