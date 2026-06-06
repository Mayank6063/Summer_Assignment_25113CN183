num = int(input("Enter decimal number: "))

binary = ""

while num > 0:
    rem = num % 2
    binary = str(rem) + binary
    num = num // 2

print("Binary =", binary)