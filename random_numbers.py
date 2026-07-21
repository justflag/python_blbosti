import random

num6 = random.randint(1,6)
num20 = random.randint(1,20)
num4 = random.randint(1,4)
print(f"Six sided dice: {num6}")
print(f"Twenty sided dice: {num20}")
print(f"Four sided dice: {num4}")


low = 1
high = 100

numhighlow = random.randint(low, high)
print(numhighlow)

randnum = random.random()
print(randnum)

options = ("rock", "paper", "scissors")
option = random.choice(options)
print(option)

cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
random.shuffle(cards)
print(cards)