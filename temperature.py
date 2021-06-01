# Program to convert degrees celsius 
#  to degrees Fahrenheit.
# Use eval to convert the string to a float.
temp = eval(input("Enter deg celsius: "))
temp2 = 9/5*temp+32
# Use the str() to convert the float to a string 
msg = "Deg Fahrenheit: " + str(temp2)
print(msg)