# Writing to a files
# This is writing a list of lines as strings
#   to a file.
cities = [ "London\n", "Canberra\n", "Seol\n"]
file1 = open('myfile.txt', 'w')
file1.writelines(cities)
file1.close()

# Reading from a file
file2 = open('myfile.txt', 'r')
lines = file2.readlines()
print(lines)
print()
# print the first element
#print(lines[0])

for line in lines:
    print(line)
    #print(line.strip())

