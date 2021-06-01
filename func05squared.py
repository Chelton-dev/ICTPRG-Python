# y = x*x  mathematical function
def square(x):
    return x*x

print( square(2) )
print( square(4) )

def dist(x,y):
    print("pause")
    return x*x + y*y

def dist2(x,y):
    return square(x)+square(y)

print()
print( "(1,1): ", dist(1,1) )
print( "(2,4): ", dist(2,4))
print( dist2(2,4))