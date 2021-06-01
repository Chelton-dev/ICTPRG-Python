try: 
    num1 = int( input("Enter num1: "))
    num2 = int( input("Enter num2: "))
    result = num1/num2

except:
    print("Error: either input or division")
else:
    print("result: ", format(result,'.2f'))

# print("result: ", format(result,'.2f'))