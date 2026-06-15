def armstrong(num):
    digits = len(str(num))
    total = sum(int(digit) ** digits for digit in str(num))
    return total == num

n = int(input("Enter a number: "))

if armstrong(n):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")