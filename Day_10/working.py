

def is_leap(year):
    """Checks if a year is a leap year or not and returns a boolean."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    is_leap_year = is_leap(year) #there is a better way to do this
    if is_leap_year == True:        #should use if is_leap(year):
        if month == 2:
            return 29
        else:
            return month_days[month - 1]
    else:
        return month_days[month - 1]            #I don't need both these elses

        
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
