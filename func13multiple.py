# Testing multiple return valued function

def get_fullname():
    first = input("Enter your first name: ")
    last = input("Enter your second name: ")
    return first, last

firstNm,lastNm = get_fullname()
print("First name: " + firstNm)
print("Last name: " + lastNm)
