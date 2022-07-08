# x(n) can be determined with the following rule:
# x(n) = x(n - 1) + x(n - 2)
#
# Create a program called fibonacci_recursive.py
#
# Requirements
#
# Given a term (n), determine the value of x(n).
# In the fibonacci_recursive.py program, create a function called fibonnaci. The function should take in an
# integer and return the value of x(n).
# This problem must be solved using recursion.

def fibonnaci(n):
    if n<=1:
        return n
    else:
        return(fibonnaci(n-1) + fibonnaci(n-2))
user_n_terms = int(input("Enter a positive integer less than 30: "))

if user_n_terms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(user_n_terms):
        print(fibonnaci(i))