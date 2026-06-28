import math #knihovna na matematicke funkce

friends = 5
friends = friends + 1
friends += 1 #plus
friends = friends - 2
friends -= 2 # minus
friends = friends * 3
friends *= 3 #krat
friends = friends / 2
friends /= 2 #deleno
friends = friends ** 2
friends **= 2 #exponent
remainder = friends % 3 #zbytek
print(friends)
print(remainder)


x = 3.14
y = -4
z = 5

result1 = round(x)
result2 = abs(y)
result3 = pow(4, 3)
result4 = max(x, y, z)
result5 = min(x, y, z)

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)

print(round(math.pi,2))
print(math.e)
result6 = math.sqrt(x)
print(result6)
result7 = math.ceil(x)
print(result7)
result8 = math.floor(x)
print(result8)