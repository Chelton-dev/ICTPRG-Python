# Read a text file and print it.
file1 = open("days01.txt")
lines = file1.readlines()
for line in lines:
    print(line)
file1.close()
