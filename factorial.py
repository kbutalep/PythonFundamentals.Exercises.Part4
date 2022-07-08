

factorial_num = int(input("Enter a number: "))

while(factorial_num != 0):
    if(factorial_num == 1):
        print(1)
    else:
        factorial = factorial_num * (factorial_num -1)
        print(factorial)
    break

if(factorial_num == 0):
    print(1)