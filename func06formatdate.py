# Format date
#
# Brief:
# Task: date formatting
# from 3 input integers.
#
# 2021-05-28
#
# formatDate(2021,5,28)

def formatDate(year,month,day):
    # local variable s1
    s1 = str(year) + "-"
    if 1 <= month < 10:
        s1 += "0"
    s1 += str(month)
    s1 += "-"
    if 1 <= day < 10:
        s1 += "0"
    s1 += str(day)
    print(s1)

# Global variable
x2 = "abc"

formatDate(2021,5,28)
formatDate(1720,5,3)