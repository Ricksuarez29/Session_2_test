##Exercise 1: FizzBuzz 1. Write a FizzBuzz Function: Create a function fizzbuzz(n) that takes an integer n as a parameter. 
# 2. Implement FizzBuzz Logic: The function should print:
# "Fizz" for multiples of 3
# "Buzz" for multiples of 5
# "FizzBuzz" for multiples of both 3 and 5
# The number itself for other numbers
# 3. Call the Function: Call the function for numbers 1 to 20.

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

for i in range(1,21):
    fizzbuzz(i)

