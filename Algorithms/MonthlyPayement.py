from Utilities import utilities
try:
    principal_loan=int(input("Enter the Principal Loan"))
    rate=float(input("Enter the Rate amount"))
    year=int(input("Enter the Year"))
    utilities.Interest(principal_loan,rate,year)
except Exception as e:
    print(e)

