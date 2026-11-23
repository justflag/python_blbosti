#exception = An eent that interrupts the flow of a program
# (ZeroDivisionError, TypeError, ValueError)
# 1. try, 2. except, 3.finally

#1 / 0 = zero division error
#1 + "1" = type error
#int("pizza") = value error

#try:
    #Try some code

#except Exception:
    #Handle an exception

#finally:
    #Do Some clean up

try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can't divide by zero.")
except ValueError:
    print("Enter only numbers.")
except Exception: #too broad, catching all exceptions
    print("Something went wrong.")
finally: #always executes without exceptions
    print("Do some cleanup here.")