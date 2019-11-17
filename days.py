import datetime

antes = '2019-06-22 12:47:23'
despues = datetime.datetime.strptime(antes, '%Y-%m-%d %H:%M:%S')

print(type(antes))
print(type(despues))
