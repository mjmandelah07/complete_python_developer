# what is oop - object oriented programming
# oop is a paradigm, a way to think our  about code  and structure code

class GamePlayer:
    def __init__(self, name):
        self.name = name

    def run(self):
        print("run", self.name)


p1 = GamePlayer("Yemi")
p1.run()


# or
class GamePlayer:
    def __init__(self, name, age):
        if age > 18:
            self.name = name
            self.age = age

    def run(self, name, age):
        print("run", self.name)
        print(f"{name} is  {age} years old")


p1 = GamePlayer("Yemi", 45)
p2 = GamePlayer("Sola", 23)
print(p1.name, "is ", p1.age, "years old")
print(p2.name)
p1.run("Dorcas", 22)


# or
class PlayerCharacter:
    membership = True  # Class Object Attributes

    def __init__(self, name, age):
        if age < 18:
            self.name = name
            self.age = age

    def run(self):
        print("run")
        return "done"

    @classmethod
    def adding(cls, num1, num2):
        return num1 + num2


p1 = PlayerCharacter("cindy", 49)
p2 = PlayerCharacter("Tom", 23)

print(p1)
print(p2)
print(p1.membership)
print(p1.adding(4, 5))
print(PlayerCharacter.adding(8, 5))


#
class PlayerCharacter:
    membership = True  # Class Object Attributes

    def __init__(self, name, age):
        if age < 18:
            self.name = name
            self.age = age

    def run(self):
        print("run")
        return "done"

    @classmethod
    def adding(cls, num1, num2):
        return cls("Teddy", num1 + num2)

    @staticmethod
    def add(num1, num2):
        return num1 + num2
        pass


p1 = PlayerCharacter("cindy", 49)
p2 = PlayerCharacter("Tom", 23)
p3 = PlayerCharacter.adding(7, 8)

print(p1)
print(p2)
print(p1.membership)
print(p1.adding(4, 5))
print(PlayerCharacter.adding(8, 5))
print(p3.age)


# function docstrings
def test(alice):
    """
     Info: This is a test function and prints parameter alice
    """

    print(alice)


test("Grace is good")
help(test)  # to search the usage
test("grace is nice".capitalize())  # capitalize only the first letter
print(test.__doc__)  # to search the usage


# inheritance -  objects take on the properties of existing objects
class User(object):
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("logged in")

    def attack(self):
        print("do nothing")
        return "DONE"


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f"{self.name} attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, arrows, email):
        super().__init__(email)
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f"{self.name} attacking with arrows:  arrows left:- {self.arrows}")


def player(char):
    char.attack()


# Object introspection- the ability to determine the type of an object at runtime
# use print(dir(wizard1)) to inspect

wizard1 = Wizard("Merlin", 50, "merlin@gmail.com")
archer1 = Archer("robin", 100, "merlin@gmail.com")

for char1 in [wizard1, archer1]:
    char1.attack()

wizard1.attack()
archer1.attack()
print(isinstance(wizard1, Wizard))
print(isinstance(archer1, User))
player(wizard1)
player(archer1)
print(wizard1.email)


# dunder methods
class Toy:
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            "name": "yoyo",
            "has_pets": False
        }

    def __str__(self):
        return f"{self.color}"

    def __len__(self):
        return 5

    def __call__(self):
        return "yes?"

    def __getitem__(self, item):
        return self.my_dict[item]


action = Toy("yellow", 10)
print(action.__str__())
print(action.__len__())
print(len(action))
print(action())
print(action["has_pets"])


# multiple inheritance
class User(object):
    def sign_in(self):
        print("logged in")
        return "done"


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"{self.name} attacking with power of {self.power}")
        return "done"


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f"{self.name} attacking with arrows:  arrows left:- {self.arrows}")
        return "done"

    def run(self):
        print("ran really fast")
        return "done"


class HybridBlog(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)
        super().__init__(name, power)


# Object introspection- the ability to determine the type of an object at runtime
# use print(dir(wizard1)) to inspect

wizard1 = Wizard("Merlin", 50)
archer1 = Archer("robin", 100)

hb1 = HybridBlog("yemi", 39, 45)

wizard1.attack()
archer1.check_arrows()
print(isinstance(wizard1, Wizard))  # check a particular values data type, return True or False
print(isinstance(archer1, Archer))
print(hb1.run())
print(hb1.check_arrows())
print(hb1.attack())
print(hb1.sign_in())


# MRO -METHOD RESOLUTION ORDER, risky to use
class A:
    num = 20


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


print(D.mro())
print(D.__mro__)
