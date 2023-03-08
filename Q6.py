# 6. Write a Python program which accepts a sequence of comma-separated
# numbers from user and generate a list and a tuple with those numbers.
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

value = input("enter the comma separated value:")
list = value.split(",")
tuple = tuple(list)
print("List:",list)
print("Tuple:",tuple)