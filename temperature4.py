# Open a file in the current director for reading.
file1 = open('temperatures.txt')
# Read the file into a string
s = file1.read()
# Take a look at the file which has been read into string s.
print(s)
print()
ti = [line.strip() for line in s]
print(ti)
file1.close()
