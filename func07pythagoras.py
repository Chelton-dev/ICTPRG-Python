# Pythagoras
# z*z = x*x + y*y
def pythagsum(x,y):
    s = x*x + y*y
    return s

# (3,4,5) triangle
# 5*5 = 3*3 + 4*4

# Expecting 25
print( pythagsum(3,4) )

# (5,12,13) - expecting 169
print( pythagsum(5,12))

def pSolver(x,y):
  # Calculate the square root with power of a half.
  z = (x*x + y*y) ** 0.5
  return z


# Expecting 5 as in (3,4,5) right angled triangle
print("solving (3,4,z)")
print( pSolver(3,4) )

print("solving for (5,12,z)")
print( pSolver(5,12))

