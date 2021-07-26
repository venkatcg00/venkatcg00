from datetime import *
current_date = date.today()
dobYear = int(input("Enter the year of birth: "))
dobMonth = int(input("Enter the month of birth: "))
dobDay = int(input("Enter the day of birth: "))
dob = date(dobYear, dobMonth, dobDay)
age = current_date - dob
print(age.days)
years = age.total_seconds() / (365.242*24*3600)
yearsInt = int(years)
months = (years - yearsInt)*12
monthsInt = int(months)
days = (months - monthsInt)*(365.242/12)
daysInt = int(days)
print("Age is %d years, %d months, %d days" % (yearsInt, monthsInt, daysInt))
