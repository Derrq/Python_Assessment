# Prompt the user for a range of numbers to evaluate
start_num = int(input("Enter the starting number: "))
end_num = int(input("Enter the ending number: "))

# Looping from start_num - end_num
for num in range(start_num, end_num):
    # if number is divisible by 3 and 5 print "FizzBuzz"
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    # if number is divisible by 3 print "Fizz"
    if num % 3 == 0 and num % 5 != 0:
        print("Fizz")
    # if number is divisible by 5 print "Buzz"
    elif num % 5 == 0 and num % 3 != 0:
        print("Buzz")
    # if number is not divisible by 3 or 5 print "Buzz"
    elif num % 5 != 0 or num % 3 != 0:
        print(num)