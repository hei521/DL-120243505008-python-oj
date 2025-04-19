def is_leap_year(year):
    return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)
 
def day_of_year(year, month, day):
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        month_days[2] = 29
    total_days = sum(month_days[1:month])
    total_days += day
    return total_days
 
year, month, day = map(int, input().split())
print(day_of_year(year, month, day))