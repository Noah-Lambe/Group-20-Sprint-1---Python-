# Description: A menu to run each program from the sprint.
# Author:      Noah Whiffen - SD12 - Group 20
# Date:        June 19th, 2024

# Import required libraries.

from Functions import BitofEverything
from Functions import FizzBizz
from Functions import Program1
from Functions import Program3
from Functions import PythonSprintQ5


# Display menu and check inputs.
while True:
    print()
    print("Midterm Sprint - Main Menu")
    print()
    print("1. Complete a travel claim.")
    print("2. Fun interview question.")
    print("3. Cool stuff with strings and dates.")
    print("4. A little bit of everything.")
    print("5. Something old, something new.")
    print("6. Quit")
    print()
    print()
    choice = input("   Enter choice (1-6): ")

    
    # Check each choice and run desired program
    if choice == "1":
        Program1.program1()
    elif choice == "2":
        FizzBizz.fizzBizz()
    elif choice == "3":
        Program3.program3()
    elif choice == "4":
        BitofEverything.bitOfEverything()
    elif choice == "5":
        PythonSprintQ5.pythonSprintQ5() # More interesting results if you use a longer input!
    elif choice == "6":
        quit()
    else:
        print("Please enter a number from 1-6.") # Error catching for invalid input.
