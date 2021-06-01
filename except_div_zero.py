num1 = int (input("Enter num1: "))
num2 = int (input("Enter num2: "))

# Problem: 
# num3 = 0/0

try:
    result = num1/num2
    print(num1,"divided by", num2, "is ", result)
except ZeroDivisionError:
    print("division by zero has occured")