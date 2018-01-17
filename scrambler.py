# Import the modules
import random
import time
from datetime import datetime
from progress.bar import Bar, IncrementalBar

timeframe = raw_input("how many minutes would you like to schedule this for? : ")

addresses = raw_input("how many addesses would you like to send payment too? : ")


#converts timeframe(seconds) to minutes
timeframe=int(timeframe)*60

publicKeys = {} # Dictionary { KEY : VALUE }

for x in range (0, int(addresses)):
	newKey = raw_input("Please type new address : ")
	while len(newKey) != 10:
		newKey = raw_input("Invalid key, try again  : ")

	sendTime = random.randint(1 ,timeframe-1)
	publicKeys[sendTime] = newKey
items = publicKeys.items()
items.sort(reverse=True)

helper = 0
timeLapsed = 0

sentTime = []
sentKeys = []

print "This will take about " + str(items[0][0] + 1) + " seconds.."

print ""

bar = IncrementalBar('Sending', max=(items[0][0]+1))

for i in range(0, items[0][0]+1):
	time.sleep(0.1)
	timeLapsed = timeLapsed + 1

	now = datetime.now()
	mm = str(now.month)
	dd = str(now.day)
	yyyy = str(now.year)
	hour = str(now.hour)
	mi = str(now.minute)
	ss = str(now.second)

	bar.next()

	currentTime = mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss
	if i in publicKeys:
		sentTo = str(publicKeys.get(i , "value"))
		sentKeys.append(sentTo)
		sentTime.append(currentTime)

		helper = helper + 1

		if int(helper) == int(addresses):
			bar.finish()
			break


print ""
print "FINISHED"
now = datetime.now()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)

print "current time: " + mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss

print ""
print 'Payments sent to :'

now = datetime.now()

mm = str(now.month)

dd = str(now.day)

yyyy = str(now.year)

hour = str(now.hour)

mi = str(now.minute)

ss = str(now.second)

for i in range(0, int(addresses)):
	print sentKeys[i] + " at " + sentTime[i]

print ""
