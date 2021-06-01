numbers = [1,2,3,4,5]
print(numbers)
numbers[2] = 90
print(numbers)

print()
num3 = list( range(2))
print(num3)


num4 = [10] * 5
print(num4)

print()
print("range(start, sentinel, step)")
num5 = list(range(0,20,5))
for k in num5:
    print(k)
print("num5:",num5)

msg2 = "A quick brown fox jumped over the lazy dog."
l2 = msg2.split()
print(l2)

# Integers in string form.
num6 = "2 5 3"
arr2 = num6.split()
print(arr2)
val = int(arr2[0])  # zero is the first element
print(val +3)  #expecting 5