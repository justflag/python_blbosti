#multiple inheritance = child class can inherit from more than one parent class
# C(A,B)

#multiple inheritance = child class caninherit from a parent which inherits form another parent
# Child(Parent) < Parent(Grandparent) < Grandparent

class Animal: #Grandparent class
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal): #Parent class
    def flee(self):
        print(f"{self.name} is fleeing.")

class Predator(Animal): #Parent class
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey): #Child class
    pass

class Hawk(Predator): #Child class
    pass

class Fish(Prey, Predator): #Child class
    pass


rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.flee()
#rabbit.hunt()
hawk.hunt()
#hawk.flee()
fish.flee()
fish.hunt()
rabbit.eat()
rabbit.sleep()
fish.eat()
fish.sleep()