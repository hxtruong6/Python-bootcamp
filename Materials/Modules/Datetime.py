import datetime

d = datetime.time(5,25,1)

today = datetime.time.today()
#print today
today.timetuple()

# date
d1 = datetime.date(2015,3,11)
d2 = d1.replace(year = 2020)