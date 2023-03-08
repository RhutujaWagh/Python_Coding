# 14. Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

from datetime import date
fdate = date(2022,11,3)
tdate = date(2023,2,28)
diff = tdate-fdate
print(diff.days)