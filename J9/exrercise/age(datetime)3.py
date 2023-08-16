import datetime
year = int(input('year(miladiy): '))
Month = int(input('Month: '))
Day = int(input('Day: '))
now = datetime.datetime.now()
year2 = int(now.year - year)
day_year = year2 * 365
month2 = int(now.month - Month)
day_month = month2 * 30
day2 = int(now.day - Day)
days = day_year + day_month + day2
week = days // 7
Second = days * 86400
print(f'You have been living for {week} weeks and {days} days and {Second}Second..')
print('good luck")')