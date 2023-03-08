
# 10.Write a Python program that accepts an integer (n) and computes the value
# of n+nn+nnn.Using String Concatenate


n = int(input("Enter the integer number for n:"))
temp = str(n)
temp1 = temp+temp
temp2 = temp+temp+temp
cal = n+int(temp1)+int(temp2)
print(cal)