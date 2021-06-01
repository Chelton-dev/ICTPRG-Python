num = ["One\n", "Two\n", "Three\n"]

# fp - stand for file pointer
with open("numbers3.txt","w") as fp:
    fp.writelines(num)

# Read in the data to fp2
with open("numbers3.txt","r") as fp2:
    lines = fp2.readlines()
print("lines: ", lines)

count=0
for line in lines:
    # count = count + 1
    count += 1   
    print("Line {}: {}".format(count,line.strip()))