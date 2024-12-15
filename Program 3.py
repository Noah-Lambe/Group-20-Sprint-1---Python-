# Description: Quarterly performance review and employment summary of specified employee.
# Author: Noah Lambe, Group 20
# Dates: June 18, 2024

# Define required libraries.
import datetime

# Start main program loop.
while True:

    # Gather and validate user inputs.
    while True:
        print()
        firstName = input("Enter the employee's first name: ").title().strip()

        if firstName == "":
            print()
            print("     Invalid entry - first name must be entered.")
        else:
            break

    while True:
        print()
        lastName = input("Enter the employee's last name: ").title().strip()

        if lastName == "":
            print()
            print("     Invalid entry - last name must be entered.")
        else:
            break

    while True:
        print()
        phone = input("Enter the employee's phone number (###-###-####): ").strip().replace("-", "")

        if phone == "":
            print()
            print("     Invalid entry - phone number must be entered.")
        elif len(phone) != 10:
            print()
            print("     Invalid entry - phone number must be ten digits.")
        else:
            break

    while True:
        print()
        startDate = input("Enter the start date of the employee (YYYY-MM-DD): ").strip()
        
        if startDate == "":
            print()
            print("     Invalid entry - date must be entered.")
        else:
            try:
                startDate = datetime.datetime.strptime(startDate, "%Y-%m-%d")
                break
            except ValueError:
                print()
                print("     Invalid entry - date entered is invalid.")

    while True:
        print()
        birthDate = input("Enter the employee's birthdate (YYYY-MM-DD): ").strip()
        
        if birthDate == "":
            print()
            print("     Invalid entry - birthdate must be entered.")
        else:
            try:
                birthDate = datetime.datetime.strptime(birthDate, "%Y-%m-%d")
                break
            except ValueError:
                print()
                print("     Invalid entry - date entered is invlaid.")

    while True:
        print()
        vacationStart = input("Enter the employee's vacation start date (YYYY-MM-DD): ").strip()

        if vacationStart == "":
            print()
            print("     Invalid entry - vacation start date must be entered.")
        else:
            try:
                vacationStart = datetime.datetime.strptime(vacationStart, "%Y-%m-%d")
                break
            except ValueError:
                print()
                print("     Invalid entry - date entered is invlaid.")

    while True:
        print()
        vacationEnd = input("Enter the employee's vacation end date (YYYY-MM-DD): ").strip()

        if vacationEnd == "":
            print()
            print("     Invalid entry - vacation end date must be entered.")
        else:
            try:
                vacationEnd = datetime.datetime.strptime(vacationEnd, "%Y-%m-%d")
                break
            except ValueError:
                print()
                print("     Invalid entry - date entered is invlaid.")

    while True:
        print()
        performance = input("Enter the employee's performance as Needs improvement(NI), OK(OK), Good(G), or Excellent(E): ").strip().upper()
        allowedResponses = ["NI", "OK", "G", "E"]

        if performance == "":
            print()
            print("     Invalid entry - performance must be entered")
        elif performance not in allowedResponses:
            print()
            print("     Invalid entry - please enter one of the following: NI, OK, G, E")
        else:
            break
    
    # Perform required proccessing.
    if performance == "NI":
        performance = "Needs Improvement"
    elif performance == "G":
        performance = "Good"
    elif performance == "E":
        performance = "Excellent"
    else:
        performance = "OK"

    fullname = f"{firstName} {lastName}"
    phoneNumber = f"({phone [0:3]}) {phone [3:6]}-{phone [6:10]}"

    currentDate = datetime.datetime.now()
    currentYear = datetime.datetime.now().year
    currentMonth = datetime.datetime.now().month
    currentDay = datetime.datetime.now().day

    if currentDate >= datetime.datetime(currentYear, 1, 1) and currentDate <= datetime.datetime(currentYear, 3, 31):
        quarter = "Q1"
    elif currentDate >= datetime.datetime(currentYear, 4, 1) and currentDate <= datetime.datetime(currentYear, 6, 30):
        quarter = "Q2"
    elif currentDate >= datetime.datetime(currentYear, 7, 1) and currentDate <= datetime.datetime(currentYear, 9, 30):
        quarter = "Q3"
    else:
        quarter = "Q4"

    performanceReview = f"{quarter}: {performance}"

    vacationLength = vacationEnd - vacationStart
    vacationSchedule = f"{vacationStart.date()} to {vacationEnd.date()}"

    tenure = (currentDate - startDate)

    if tenure >= datetime.timedelta(days=7305):
        payRate = "$50.00/hr"
    elif tenure >= datetime.timedelta(days=5478):
        payRate = "$40.00/hr"
    elif tenure >= datetime.timedelta(days=3652):
        payRate = "$30.00/hr"
    elif tenure >= datetime.timedelta(days=1826):
        payRate = "$25.00/hr"
    else:
        payRate = "$20.00/hr"

    birthday = f"{datetime.datetime.strftime(birthDate, '%B %d')}"

    if currentDate < birthDate.replace(year=currentYear):
        nextBirthday = birthDate.replace(year=currentYear) - currentDate
    else:
        nextBirthday = birthDate.replace(year=currentYear + 1) - currentDate

    if nextBirthday.seconds > 0:
        daysUntilNextBirthday = nextBirthday.days + 1
    else:
        daysUntilNextBirthday = nextBirthday.days

    retirement = birthDate.replace(year = birthDate.year + 65)
    retirementDSP = retirement.date()
    daysUntilRetirement = retirement - currentDate

    if daysUntilRetirement.seconds > 0:
        daysUntilRetirement = daysUntilRetirement.days + 1

    # Display outputs.
    print()
    print(f"   --- Performance overview and Employment summary ---")
    print(f"   Current Date:              {currentDate.date()}")
    print(f"   Full Name:                 {fullname}")
    print(f"   Phone:                     {phoneNumber}")
    print(f"   Start Date:                {startDate.date()}")
    print(f"   Birth Date:                {birthDate.date()}")
    print(f"   Next Birthday:             {daysUntilNextBirthday} days away")
    print(f"   Pay Rate:                  {payRate}")
    print(f"   Vacation Schedule:         {vacationSchedule}")
    print(f"   Vacation Length:           {vacationLength.days} days")
    print(f"   Performance Review:        {performanceReview}")
    print(f"   Tenure:                    {tenure.days} days")
    print(f"   Retirement Date:           {retirementDSP}")
    print(f"   Days Until Retirement:     {daysUntilRetirement} days")
    print(f"   ---------------------------------------------------")

    # Concluding program.
    while True:
        print()
        finish = input("Would you like to continue? (Y/N): ").upper()

        if finish == "":
            print()
            print("Invalid entry - continue selection must be entered.")
        elif finish != "Y" and finish != "N":
            print()
            print("Invalid entry - selection must be yes or no (Y/N).")
        else:
            break

    if finish == "N":
        break

print()
print("Have a great day!")
print()