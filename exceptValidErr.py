try:
    hours = int( input("How many hours did you work?: "))
    pay_rate = float(input("Enter hourly pay: "))
    gross_pay = hours * pay_rate

    print("Gross pay: $", format(gross_pay,'.2f'), sep='')
except ValueError as err:
    print("Error, hours worked and pay should be valid numbers.")
    print(err)

