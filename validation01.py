validInteger = False

while not validInteger:
    age = input("How old are you? ")
    if age.isdigit():
        validInteger = True
    else:
        print("You must enter a valid number")

print("You are " + age)