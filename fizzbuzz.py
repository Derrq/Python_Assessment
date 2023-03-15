# Given number n.
# Prompt user for input
# Looping from 0-n
# if number is divisible by 3 print "Fizz"
# if number is divisible by 5 print "Buzz"
# if number is divisible by 3 and 5 print "FizzBuzz"
# if number is divisible by 3 or 5 return Number

n = 100

for num in range(1, (n+1)):
    # if number is divisible by 3 and 5 print "FizzBuzz"
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    # if number is divisible by 3 print "Fizz"
    if num % 3 == 0:
        print("Fizz")
    # if number is divisible by 5 print "Buzz"
    elif num % 5 == 0:
        print("Buzz")
    # if number is divisible by 3 or 5 return Number
    else:
        print(num)