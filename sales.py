# Example p.13
num_days = int(input("For how many days do you have sales? :"))
sales_file = open('sales.txt','w')
for count in range(1,num_days+1):
    sales=float(input('Enter the sales for day #: '+ str(count) + ':'))
    sales_file.write(str(sales)+'\n')
sales_file.close()

print("data is written to file sales.txt")
sales_file1=open('sales.txt','r')
for count in range (1,num_days+1):
    sales=float(sales_file1.readline())
    print(sales)
sales_file.close()