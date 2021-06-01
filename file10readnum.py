infile = open('numbers2.txt')
num1 = int(infile.readline())
num2 = int(infile.readline())
num3 = int(infile.readline())
infile.close()
total = num1+num2+num3
print("numbers: ", num1,num2,num3)
print("total: ",total)