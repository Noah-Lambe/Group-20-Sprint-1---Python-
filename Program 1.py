# Description: A program for NL Chocolate Company to process the travel claims of their employees.
# Author: Noah Lambe, Group 20
# Dates: June 17, 2024

# Define required libraries.
import datetime

# Define program constants.
PER_DIEM_RATE = 85.00
PERSONAL_VEHICLE_RATE = 0.17
RENTAL_CAR_RATE = 65.00
EXTENDED_STAY_BONUS_RATE = 100.00
PERSONAL_VEHICLE_BONUS_RATE = 0.04
EXECUTIVE_BONUS_RATE = 45.00
HOLIDAY_TRAVEL_BONUS = 50.00
TAX_RATE = 0.15

# Define program functions.

# Start main program loop.
while True:

    # Gather and validate user inputs.
    while True:
        print()
        employeeNumber = input("Enter the employee's identification number (#####): ").strip()

        if employeeNumber == "":
            print()
            print("     Invalid entry - employee number must be entered.")
        elif employeeNumber.isdigit() == False:
            print()
            print("     Invalid entry - characters entered must be numbers.")
        elif len(employeeNumber) != 5:
            print()
            print("     Invalid entry - employee number must be 5 digits.")
        else:
            break
    
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
        tripLocation = input("Enter the location of the business trip: ").title().strip()

        if tripLocation == "":
            print()
            print("     Invalid entry - trip location must be entered.")
        else:
            break

    while True:
        print()
        startDate = input("Enter the start date of the business trip (YYYY-MM-DD): ").strip()
        
        if startDate == "":
            print()
            print("     Invalid entry - date must be entered.")
        else:
            try:
                startDate = datetime.datetime.strptime(startDate, "%Y-%m-%d")
                break
            except ValueError:
                print("     Invalid entry - date entered is invlaid.")

    while True:
        print()
        endDate = input("Enther the end date of the business trip (YYYY-MM-DD): ").strip()

        if endDate == "":
            print()
            print("     Invalid entry - date must be entered.")
        else:
            try:
                endDate = datetime.datetime.strptime(endDate, "%Y-%m-%d")
                break
            except ValueError:
                print("     Invalid entry - date entered is invlaid.")

    while True:
        print()
        rentalStatus = input("Enter if car is owned by employee or rented (O/R): ").upper()

        if rentalStatus == "":
            print()
            print("     Invalid entry - rental status must be entered.")
        elif rentalStatus != "O" and rentalStatus != "R":
            print()
            print("     Invalid entry - entry must be owned or rented (O/R).")
        else:
            break

    while True:
        print()
        totalKmTravelled = int(input("Enter the total kilometers travelled on the trip: ").strip())

        if totalKmTravelled == "":
            print()
            print("     Invalid entry - km travelled must be entered.")
        elif totalKmTravelled > 2000:
            print()
            print("     Invalid entry - km cannot exceed 2000.")
        else:
            break

    while True:
        print()
        claimType = input("Enter the type of claim, Standard or Executive (S/E): ").upper()

        if claimType == "":
            print()
            print("     Invalid entry - claim type must be entered.")
        elif claimType != "S" and claimType != "E":
            print()
            print("     Invalid entry - claim type must be standard or executive (S/E).")
        else:
            break

    # Perform required calculations.
    tripDuration = (endDate - startDate).days
    perDiem = tripDuration * PER_DIEM_RATE
    rentalCost = 0
    mileageCost = 0

    if rentalStatus == "R":
        rentalCost = tripDuration * RENTAL_CAR_RATE
    else:
        mileageCost = totalKmTravelled * PERSONAL_VEHICLE_RATE

    bonus = 0

    if tripDuration > 3:
        bonus += EXTENDED_STAY_BONUS_RATE

    if totalKmTravelled > 1000 and rentalStatus == "O":
        bonus += (totalKmTravelled * PERSONAL_VEHICLE_BONUS_RATE)

    if claimType == "E":
        bonus += (tripDuration * EXECUTIVE_BONUS_RATE)

    year = datetime.datetime.now().year

    if startDate >= datetime.datetime(year, 12, 15) and startDate <= datetime.datetime(year, 12, 22):
        bonus += HOLIDAY_TRAVEL_BONUS
    
    claimAmount = perDiem + mileageCost + bonus
    tax = claimAmount * TAX_RATE
    claimTotal = claimAmount + tax

    # Format outputs.
    if rentalStatus == "R":
        rentalStatus = "Rental"
    else:
        rentalStatus = "Owned"

    if claimType == "S":
        claimType = "Standard"
    else:
        claimType = "Executive"
    
    perDiemDSP = "${:,.2f}".format(perDiem)
    rentalCostDSP = "${:,.2f}".format(rentalCost)
    mileageCostDSP = "${:,.2f}".format(mileageCost)
    bonusDSP = "${:,.2f}".format(bonus)
    claimAmountDSP = "${:,.2f}".format(claimAmount)
    taxDSP = "${:,.2f}".format(tax)
    claimTotalDSP = "${:,.2f}".format(claimTotal)

    # Display outputs.
    print()
    print()
    print("Employee Information:")
    print()
    print(f"Employee Number:             {employeeNumber}")
    print(f"First Name:                  {firstName}")
    print(f"Last Name:                   {lastName}")
    print(f"Trip Location:               {tripLocation}")
    print(f"Trip Start Date:             {startDate.strftime('%Y-%m-%d')}")
    print(f"Trip End Date:               {endDate.strftime('%Y-%m-%d')}")
    print(f"Rental Status:               {rentalStatus}")
    print(f"Total Kilometers Travelled:  {totalKmTravelled}")
    print(f"Claim Type:                  {claimType}")
    print()
    print()
    print("Calculated Values:")
    print()
    print(f"Trip Duration:               {tripDuration} days")
    print(f"Per Diem:                    {perDiemDSP:>10s}")
    if rentalCost > 0:
        print(f"Rental cost:                 {rentalCostDSP:>10s}")
    if mileageCost > 0:
        print(f"Mileage Cost:                {mileageCostDSP:>10s}")
    print(f"Bonus:                       {bonusDSP:>10s}")
    print(f"Claim Amount:                {claimAmountDSP:>10s}")
    print(f"Tax:                         {taxDSP:>10s}")
    print(f"Claim Total:                 {claimTotalDSP:>10s}")
    print()

    # Conclude program.
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