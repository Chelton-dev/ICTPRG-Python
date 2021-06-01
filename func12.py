def is_odd(number):
    if (number % 2) != 0:
        status=True
    else:
        status=False
    return status

print( is_odd(2))
print( is_odd(3))
print( is_odd(4))

# Expecting
# False
# True
# False

def is_odd_print(number):
    print(str(number) + ": " + str(is_odd(number)) )

is_odd_print(2)
is_odd_print(3)
is_odd_print(4)
is_odd_print(5)

