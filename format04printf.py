# Testing formatting with printf derivations

ruler = "012345678901234567890123456789"
print(ruler)

# String printing is with formatter %s

# string 
s1 = "abcdef"
print("%s" % s1)
# Right side alignment
print("*%10s*" % s1)
# Left side alignment
print("*%-10s*" % s1)




# integer printing is with formatter %d

print(ruler)

num = 4567
print("%d" % num)
# Right align
print("*%8d*" % num)
# Left align
print("*%-8d*" % num)

print(ruler)
# float printing is with formatter %f
pi = 3.141592654
print("%f" % pi)
print("*%10.2f*" % pi)
print("*%-10.2f*" % pi)
print("*%10.3f*" % pi)
print("*%-10.3f*" % pi)
print("*%10.4f*" % pi)
print("*%-10.4f*" % pi)

print("----------------")
print("%10.2f" % 2.718281828 )
print("%10.2f" % 120.25)

