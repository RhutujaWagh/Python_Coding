# 16. Write a Python program to get the difference between a given number and 17, if
#     the number is greater than 17 return double the absolute difference.

m = 17
n = int(input("Enter the integer number:"))

def differnce(n):
    if n<=17:
        return m-n
    else:
        return (n-m)*2

print(differnce(n))

