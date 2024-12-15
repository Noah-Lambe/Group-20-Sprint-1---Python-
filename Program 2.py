# Description: Sprint 1 - FizzBizz
# Name: Jonathan Strickland, Noah Whiffen, Noah Lambe
# Date: June 15th 2024

# Start main loop
for num in range(1, 101):
    if num % 5 == 0 and num % 8 == 0:
        msg = "FizzBizz"
    elif num % 5 == 0:
        msg = "Fizz"
    elif num % 8 == 0:
        msg = "Bizz"
    else:
        msg = str(num)

    print(msg)