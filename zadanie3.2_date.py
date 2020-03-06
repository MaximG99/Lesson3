#Напечатайте в консоль даты: вчера, сегодня, месяц назад
#Превратите строку "01/01/17 12:10:03.234567" в объект datetime

from datetime import date, datetime, timedelta

 #1.сегодня 
dt_today = datetime.now()
print(dt_today)

#2.вчера
dt_yesterday = dt_today - timedelta(days=1)
print(dt_yesterday)

#3.месяц назад  
dt_month = dt_today - timedelta(days=30)
print(dt_month)

#4 строка в дату
date_string = '01/01/2017 12:10: 03.234567'
date_converted = datetime.strptime(date_string, '%m/%d/%Y %H:%M:%S.%f')
print(date_converted)




