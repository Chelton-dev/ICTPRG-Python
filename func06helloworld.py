# Example hello world input/oupt

# One paramter input, no output.
def inOnly(s):
    print(s)

#inOnly("hello world")
#inOnly("End of the world")

def inOut(s):
    msg = s + ", world!"
    return msg

# Both input (one parameter) and oupu
s2 = inOut("Hello")
print(s2)
print( inOut("Hello") )