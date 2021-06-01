L = ["One\n", "Two\n", "Three\n"]

with open("numberstrings.txt", "w") as fp:
    fp.writelines(L)
fp.close()

print()
count=0
print("Using .readlines() to read the file")

with open("numberstrings.txt") as fp2:
    lines = fp2.readlines()
fp2.close()

for line in lines:
    count += 1
    print("Line {}: {}".format(count,line.strip()))
