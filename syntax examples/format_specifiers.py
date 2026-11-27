# format specifiers = {value:flags} format a value based on what flags are inserted
#.(number)f = round to that many decimal places
#:(number) = allocate that many spaces
#:03 = allocate and zero pad that many spaces
#:< = left justify
#:> = right justify
#:^= center align
#:+ = use a plus sign to indicate positive value
#:= = place sign to leftmost position
#: = insert a space before positive numbers
#:, = comma separator

price1 = 3000.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is ${price1:.1f}")
print(f"Price 2 is ${price2:.2f}")
print(f"Price 3 is ${price3:.3f}")
print("")
print(f"Price 1 is ${price1:10}")
print(f"Price 2 is ${price2:20}")
print(f"Price 3 is ${price3:30}")
print("")
print(f"Price 1 is ${price1:010}")
print(f"Price 2 is ${price2:020}")
print(f"Price 3 is ${price3:030}")
print("")
print(f"Price 1 is ${price1:<10}")
print(f"Price 2 is ${price2:<20}")
print(f"Price 3 is ${price3:<30}")
print("")
print(f"Price 1 is ${price1:>10}")
print(f"Price 2 is ${price2:>20}")
print(f"Price 3 is ${price3:>30}")
print("")
print(f"Price 1 is ${price1:^10}")
print(f"Price 2 is ${price2:^20}")
print(f"Price 3 is ${price3:^30}")
print("")
print(f"Price 1 is ${price1:+}")
print(f"Price 2 is ${price2:+}")
print(f"Price 3 is ${price3:+}")
print("")
print(f"Price 1 is ${price1: }")
print(f"Price 2 is ${price2: }")
print(f"Price 3 is ${price3: }")
print("")
print(f"Price 1 is ${price1:,}")
print(f"Price 2 is ${price2:,}")
print(f"Price 3 is ${price3:,}")
print("")
print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}")