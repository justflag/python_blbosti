# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local > Enclosed > Global > Built-in

# functions cant see inside of other functions
def func1():
    x = 1 #enclosed scope
    def func2():
        x = 2 #local scope
        print(x)
    func2()
func1()

x = 3 # global scope
def func3():
    print(x)
def func4():
    print(x)
func3()
func4()

from math import e
def func5():
    print(e) #built-in scope
#e = 3 #global scope - prints first because it checks before built-in
func5()