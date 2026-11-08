# for loop = execute a block of code a fixed number of times
# iterate over a range, strings, sequence

for x in reversed(range(1, 11,)):
    print(x)
print("Happy New Year!")

for x in range(1,11,2):
    print(x)

credit_card = "1234-5678-901-3456"

for x in credit_card:
    print(x)

for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)

for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)