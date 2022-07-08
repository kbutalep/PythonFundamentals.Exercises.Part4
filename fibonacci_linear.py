# x(n) can be determined with the following rule:
# x(n) = x(n - 1) + x(n - 2)

user_n_terms = int(input("Enter a positive integer less than 30: "))

num1 = 0
num2 = 1
count = 0

if (user_n_terms <= 0):
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    while(count < user_n_terms):
        print(num1)
        next_num = num1 + num2
        num1 = num2
        num2 = next_num
        count += 1