def reverse_name(first,last):
    print(last,first)

#first_name = input("Enter first name: ")
#last_name = input("Enter your last name: ")
#print("Your name reversed is: ")
#reverse_name(first_name,last_name)

# return "Smith Fred" from
#  reverse_name2('Fred','Smith')
def reverse_name2(first,last):
    s = last
    s += " "
    s += first
    #print(s)
    return s

print( reverse_name('Fred','Smith') )

first_name = input("Enter first name: ")
last_name = input("Enter your last name: ")
msg = "Your name reversed is: " 
msg += reverse_name2(first_name,last_name)
print(msg)

print("Your name reversed is: " + reverse_name2(first_name,last_name) )

