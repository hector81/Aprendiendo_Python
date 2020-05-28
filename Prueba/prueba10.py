import datetime

date1 = datetime.datetime.now()

# Esperamos unos segundos…



date2 = datetime.datetime(2020,3,28)
delta = date2 - date1
print(delta.days,delta.seconds,delta.microseconds)
