from datetime import datetime
from datetime import timedelta
# from datetime import date
# from datetime import time

# import datetime
# tüm hepsi import edilir.

simdi = datetime.now()
simdi = datetime.today()

result = datetime.now()
result = simdi.year
result = simdi.month
result = simdi.day
result = simdi.hour       #saat
result = simdi.minute     #dakika
result = simdi.second     #saniye

result = datetime.ctime(simdi)      # açıklayıcı bilgi verir
result = datetime.strftime(simdi,'%Y')      # yıl
result = datetime.strftime(simdi,'%X')      # saat
result = datetime.strftime(simdi,'%d')      # gün
result = datetime.strftime(simdi,'%A')      # gün bilgisimi yazılı verir
result = datetime.strftime(simdi,'%B')      # ay bilgisini yazılır verir
result = datetime.strftime(simdi,'%Y %B %A')

t = '15 April 2019 hour 10:12:30'
result = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
result = result.year

birthday = datetime(1983,5,9,12,30,10)

result = datetime.timestamp(birthday) # saniye
result = datetime.fromtimestamp(result) # saniye to datetime
result = datetime.fromtimestamp(0)

result = simdi - birthday # timedelta

# result = result.days
# result = result.seconds
# result = result.microseconds
print(simdi)

# result = simdi + timedelta(days=10)
# result = simdi + timedelta(days=730, minutes = 10)

result = simdi - timedelta(days = 10)

print(result)