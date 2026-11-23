weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds?: (k or l)").lower()

if unit == "k":
    weight *= 2.205
    unit = "lbs."
    print(f"Your weight is: {round(weight,1)} {unit}")
elif unit == "l":
    weight /= 2.205
    unit = "kg."
    print(f"Your weight is: {round(weight,1)} {unit}")
else:
    print(f"{unit} was not valid")

