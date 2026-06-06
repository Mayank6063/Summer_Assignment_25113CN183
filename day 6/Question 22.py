binary = input("Enter binary number: ")

decimal = 0
power = 0

for i in binary[::-1]:
    decimal = decimal + int(i) * (2 ** power)
    power += 1

print("Decimal =", decimal)

