def main():
    val = int( input("Enter an integer: "))
    show_square(val)

def show_square(num):
    res = num * num
    print( 'The square of ' + str(num) + " is " + str(res))

main()