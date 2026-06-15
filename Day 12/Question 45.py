def palindrome(num):
    return str(num) == str(num)[::-1]

n = int(input("Enter a number: "))

if palindrome(n):
    print("Palindrome")
else:
    print("Not Palindrome")
    