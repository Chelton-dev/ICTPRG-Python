mylist =["Fred:123", "Smith:475" ]

checkUser = "Smith"
for i in mylist:
        arr=i.split(":")
        if arr[0] == checkUser:
            print("found")
            