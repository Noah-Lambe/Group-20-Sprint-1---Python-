# Description: Sprint 1 - A Little Bit of Everything
# Name: Jonathan Strickland, Noah Whiffen, Noah Lambe
# Date: June 18th 2024

def bitOfEverything():

    import datetime

    print()
    print("Welcome to the XYZ Company's Maintenance Schedule")

    # Input for cost of the equipment
    while True:
        try:
            costofmain = float(input("Enter the cost of the equipment: "))
            if costofmain <= 0:
                print("Invalid cost. Please enter a positive number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Input for purchase date
    while True:
        try:
            dateofmain = input("Enter the purchase date (YYYY-MM-DD): ")
            purchasedate = datetime.datetime.strptime(dateofmain, '%Y-%m-%d')
            break
        except ValueError:
            print("Invalid date format. Please enter the date as YYYY-MM-DD.")

    # Calculating maintenance dates
    basicclean = purchasedate + datetime.timedelta(days=10)
    tubecheck = purchasedate + datetime.timedelta(weeks=3)
    majorinspect = purchasedate + datetime.timedelta(weeks=26)

    # Calculating amortization
    uselife = 15 * 12
    salvalue = costofmain * 0.10
    amort = (costofmain - salvalue) / uselife

    # Outputting results
    print()
    print("Maintenance Schedule and Amortization Details")
    print("---------------------------------------------")
    print(f"Purchase Cost: ${costofmain:.2f}")
    print(f"Purchase Date: {purchasedate.strftime('%Y-%m-%d')}")
    print(f"Basic Cleaning Date: {basicclean.strftime('%Y-%m-%d')}")
    print(f"Tube and Fluid Check Date: {tubecheck.strftime('%Y-%m-%d')}")
    print(f"Major Inspection Date: {majorinspect.strftime('%Y-%m-%d')}")
    print(f"Salvage Value: ${salvalue:.2f}")
    print(f"Monthly Amortization: ${amort:.2f}")
    print()
