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

timeframe = raw_input("how many minutes would you like to schedule this for? ")

addresses = raw_input("how many addesses would you like to send payment too? ")


#converts timeframe(seconds) to minutes 
timeframe=int(timeframe)*60

publicKeys = {}

for x in range (0, int(addresses)):
	newKey = raw_input("Please type address ")# + str(x+1) + " of " + int(addresses)
	while len(newKey) != 10:
		print ("Please enter a proper key")
		newKey = raw_input("Please type address ")# + str(x+1) + " of " + int(addresses)

	publicKeys[newKey] = random.randint(1 ,timeframe)
print publicKeys

	

#executable
for x in range(0, timeframe):
	time.sleep(0.5)
	if x in publicKeys.values():
		print 'SENT PAYMENT'
	print "We're on time %d" % (x+1)


	#if x = publicKeys.get('KEY[' + str(x) +']', 
	
#print randTimeframe


now = datetime.now()

mm = str(now.month)

dd = str(now.day)

yyyy = str(now.year)

hour = str(now.hour)

mi = str(now.minute)

ss = str(now.second)

print mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss


