# 7. Write a Python program to accept a filename from the user and print the
# extension of that.

filename = input("Input the filename:")
f_extns = filename.split(".")
print("The file is:"+repr(f_extns[-1]))