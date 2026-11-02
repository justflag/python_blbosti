#*args = allows you to pass multiple non-key arguments
#**kwargs = allows you to pass multiple keyword-arguments
#* unpacking operator

def add(*nums):
    total = 0
    #print(type(args))
    for num in nums:
        total += num
    return total

#print(add(1, 2, 3))
print(add(1,2,50))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Mr. " "Stepan","Nevim", "Bargl")
print(" ")
def print_address(**kwargs):
    #print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key}:{value}")

print_address(street="U Hrbitova", 
              city="Jihlava", 
              country="Czechia", 
              zip="58601")

print()

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    #for value in kwargs.values():
    #    print(value, end=" ")
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('country')}, {kwargs.get('zip')}")

shipping_label("Stepan", "Bargl",
        country="Czeciha",
        city="Jihlava",
        street="U Hrbitova",
        #apt="4",
        pobox="PO Box #101",
        zip="58601")