validLength = False

while not validLength:
    password = input("Enter password at least 6 characters: ")
    if len(password) >= 6:
        validLength = True
    else:
        print("Your password is too short: ")      
        
print("Your password is " + password)

