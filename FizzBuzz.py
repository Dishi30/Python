#if the number is divisible by 3 print "Fizz", if divisible by 5 print "Buzz", if divisible by both print "FizzBuzz"
target = int(input("Enter the range: "))
for i in range(1,target + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
