# Author:Stuart Daniells
# Date: 2021-10-24

print("**********BUYING THE CAR************\n")

# User enters car price, calculating tax for the car and displaying it with a formating of 
# 2 decimal places with input validation
carPrice = float(input("Please enter purchase price of the car: "))
while (carPrice < 0):
    carPrice = float(input("Please enter a value greater than 0: "))
    
carTax = carPrice * 0.13
carTax = float(format(carTax, '.2f'))
print("Taxes to be added (13%):", carTax)

# Calculating total car price with tax and displaying it with a formating of 2 decimal places
totalCarPrice = carPrice + carTax
totalCarPrice = float(format(totalCarPrice, '.2f'))
print("Purchase price with taxes:", totalCarPrice)

# User enters loan interest rate and duration of loan in years with input validation
loanInterestRate = float(input("Please enter loan rate (as a %): ")) / 100
while (loanInterestRate < 0):
    loanInterestRate = float(input("Please enter a value greater than 0: "))
    
loanYears = int(input("Please enter duration of the loan (years): "))
while (loanYears < 0):
    loanYears = float(input("Please enter a value greater than 0: "))

loanMonths = loanYears * 12

# Calculating monthly payments for the cars outright purchase and displaying it with 
# a formating of 2 decimal places 
monthlyPayments = ((loanInterestRate / 12) * totalCarPrice) / (1 - ((1 + (loanInterestRate/12))**(-loanMonths)))
monthlyPayments = float(format(monthlyPayments, '.2f'))
print("\nMonthly cost of purchase:", monthlyPayments)

print("\n*********LEASING THE CAR************\n")

# User enters the monthly lease price for the car and convert it with to a formating of 
# 2 decimal places with input validation
monthlyLeasePrice = float(input("Monthly Lease Price: "))
while (monthlyLeasePrice < 0):
    monthlyLeasePrice = float(input("Please enter a value greater than 0: "))
    
monthlyLeasePrice = float(format(monthlyLeasePrice, '.2f'))

# Calculating lease tax for the car and displaying it with a formating of 2 decimal places
leaseTax = monthlyLeasePrice * 0.13
leaseTax = float(format(leaseTax, '.2f'))
print("Taxes to be added (13%):", leaseTax)

# Calculating the total lease of the car with tax and displaying it
totalLeaseCost = monthlyLeasePrice + leaseTax
print("Total Monthly lease cost:", totalLeaseCost)

# Comparing which is the cheaper option for the user, either lease or outright purchase
print("\n*********COMPARISON***************")

# Inputing years the user wants to keep the car, and displaying the payments for lease and 
# outright car purchase in a tabular table format (without the lines) with input validation

years = int(input("\nPlease enter the duration you plan on keeping the car (years): \n"))
while (years < 0):
    years = float(input("Please enter a value greater than 0: "))
    
months = 12
displayedLeave = totalLeaseCost
displayedPayments = monthlyPayments
nextDisplayPayment = 0

# Tabular table display of monthly lease and outright car purchase
print("\n----------------------------------------------------------")
print("Comparison table between leasing and outright purchasing")
print("----------------------------------------------------------")

print("\nYear \t Month \t Lease Total \t Purchase Total")

for year in range(1, years+1):
    for month in range(1, months+1):
        
        # If user completes total car payment for outright purchase, we stop displaying in table
        # below if else statement does that
        if(nextDisplayPayment != displayedPayments):
            print(year, month, (displayedLeave), (displayedPayments), sep=" \t ")
        else:
            print(year, month, (displayedLeave), sep=" \t ")
            
        # To display month wise payments for lease and car purchase
        nextDisplayPayment = displayedPayments
        displayedLeave += totalLeaseCost
        
        if (displayedPayments <= totalCarPrice):
            displayedPayments += monthlyPayments
            displayedPayments = float(format(displayedPayments, '.2f'))
        

finalLease = years * months * totalLeaseCost

# Checking to see the more reasonable option, whether lease or outright car purchase
if (totalCarPrice > finalLease): 
    print("\nBased on the information provided, if you plan to keep your vehicle for", years ," years, it is cheaper to lease.")
elif (finalLease > totalCarPrice):
    print("\nBased on the information provided, if you plan to keep your vehicle for", years ," years, it is cheaper to purchase the car outright.")
else:
    print("Both are equal, so going for either which option is good")



