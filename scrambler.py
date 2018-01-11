# Import the modules
import random
import time
from datetime import datetime

now = datetime.now()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)

print mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss

timeframe = raw_input("how many minutes would you like to schedule this for? : ")

addresses = raw_input("how many addesses would you like to send payment too? : ")


#converts timeframe(seconds) to minutes
timeframe=int(timeframe)*60

publicKeys = {}

for x in range (0, int(addresses)):
	newKey = raw_input("Please type address : ")# + str(x+1) + " of " + int(addresses)
	while len(newKey) != 10:
		print ("Please enter a proper key")
		newKey = raw_input("Please type a valid address : ")# + str(x+1) + " of " + int(addresses)

	sendTime = random.randint(1 ,timeframe-1)
	#publicKeys[newKey] = random.randint(1 ,timeframe)
	publicKeys[sendTime] = newKey
items = publicKeys.items()
items.sort()

print items
print publicKeys

helper = 0
timeLapsed = 0

for i in range(0, timeframe):
	time.sleep(0.1)
	timeLapsed = timeLapsed + 1
	if i in publicKeys:
		print 'SENT PAYMENT TO: '
		print publicKeys.get(i , "value")
		print ''
		helper = helper + 1

		if int(helper) == int(addresses):
			break

	now = datetime.now()
	mm = str(now.month)
	dd = str(now.day)
	yyyy = str(now.year)
	hour = str(now.hour)
	mi = str(now.minute)
	ss = str(now.second)
	print mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss
	#if x = publicKeys.get('KEY[' + str(x) +']',

#print randTimeframe

print 'Completed payments'
print timeLapsed

now = datetime.now()

mm = str(now.month)

dd = str(now.day)

yyyy = str(now.year)

hour = str(now.hour)

mi = str(now.minute)

ss = str(now.second)

print mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss
