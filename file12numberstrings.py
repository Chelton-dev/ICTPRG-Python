# https://www.pythonforbeginners.com/files/with-statement-in-python

# Assumes numberstring.txt exists
count = 0
with open("numberstrings.txt") as fp:
    while True:
        count += 1
        line = fp.readline()

        # Test to exit
        if not line:
            break

        print("Line {}: {}".format(count,line.strip()))
#fp.close()

print()
count = 0
print("Using for loop to iterate")
with open("numberstrings.txt") as fp2:
    for line in fp2:
        count += 1
        print("Line {}: {}".format(count,line.strip()))
#fp2.close()