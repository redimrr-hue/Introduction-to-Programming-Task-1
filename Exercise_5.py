month_days = {
    1: 31,  # January
    2: 28,  # February (default, non-leap year)
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31, # October
    11: 30, # November
    12: 31  # December
}
month = int(input("Enter a month number (1-12): "))
if month in month_days:
    if month == 2:
        leap_year = input("Is it a leap year? (yes/no): ").lower()
        if leap_year == "yes":
            print("February has 29 days.")
        else:
            print("February has 28 days.")
    else:
        print(f"This month has {month_days[month]} days.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")