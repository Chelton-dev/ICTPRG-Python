# Basic read of csv file - does not delete whitespace
#  and blank lines

# read data01.csv as a comma separated csv file:
#   name,id

# readlines() reads to EOF but does not close the file.
file1 = open("data01.csv","r")
lines = file1.readlines()
print("lines:")
print(lines)

print("lines2:")
lines2 = file1.read()
print(lines2)

print("Query if file is closed")
print(file1.closed)
file1.close()
print("closed file")
print(file1.closed)


# Make a new list
lines3 = []
for line in lines:
    line2 = line.strip()
    print(line2)
    if line2 != "":
        lines3.append(line2)

print(lines3)
# Data is still in strings.
# Could use split