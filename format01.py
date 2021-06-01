# https://pyformat.info

# f - float e.g. .2f is two places

mypi = 3.141592654
#print("format(x,'.<decimal places>f)' formatting")
print('mypi: ', format(mypi,'.2f'))
print('mypi: ', format(mypi,'.3f'))
print('mypi: ', format(mypi,'.4f'))

#print("Same formatting with {:.<decimal places>f}")
print("mypi: {:.2f}".format(mypi))
print("mypi: {:.3f}".format(mypi))
print("mypi: " + "{:.4f}".format(mypi))

print()
print("01234567890123456789")
print("mypi: {:10.2f}".format(mypi))
print("mypi: {:10.3f}".format(mypi))
print("mypi: {:10.4f}".format(mypi))


