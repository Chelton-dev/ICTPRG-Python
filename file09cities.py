cities = ["London\n", "Camberra\n", "Seoul\n"]
file1 = open('myfile2.txt','w')
file1.writelines(cities)
file1.close()

file2 = open('myfile2.txt','r')
lines = file2.readlines()
print(lines)
file2.close()


print()
count = 0
for line in lines:
    #print(line)
    #print(line.strip())
    print("Line {}: {}".format(count,line.strip()))
    count = count+1