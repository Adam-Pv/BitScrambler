# Import the modules
import random
import time
from datetime import datetime
from progress.bar import Bar, IncrementalBar

def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def getTimeStamp():
	now = datetime.now()
	mm = str(now.month)
	dd = str(now.day)
	yyyy = str(now.year)
	hour = str(now.hour)
	mi = str(now.minute)
	ss = str(now.second)
	currentTime = mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss
	return currentTime

# Sets how much cyrpto to send
sendAmount = raw_input("How much crypto are you sending? ")
while isFloat(sendAmount) == False or sendAmount.isdigit() == False:
	print("Invalid entry!")
	sendAmount = raw_input("How much crypto are you sending? ")

# Sets how long to space out transcation
timeframe = raw_input("How many minutes would you like to schedule this for? : ")
while timeframe.isdigit() == False or int(timeframe) == 0:
	print ("Invalid entry!")
	timeframe = raw_input("How many minutes would you like to schedule this for? : ")
#converts timeframe(seconds) to minutes
timeframe=int(timeframe)*60

# Sets how many addressess to send too
addresses = raw_input("How many addresses would you like to send payment too? : ")
while addresses.isdigit() == False or int(addresses) == 0:
	print ("Invalid entry!")
	#print ("Addresses limited to 30!") Should this even be implemented?
	addresses = raw_input("How many addesses would you like to send payment too? : ")

# Sets the addressess
publicKeys = {} # Dictionary { KEY : VALUE }
for x in range (0, int(addresses)):
	newKey = raw_input("Please type recipient address : ")
	while len(newKey) != 10:
		newKey = raw_input("Invalid entry try again : ")
	sendTime = random.randint(1 ,timeframe-1)
	if x == 0:
		sendTime = 1
	publicKeys[sendTime] = newKey
items = publicKeys.items()
items.sort(reverse=True)

# Sends the transactions
timeLapsed = 0
sentTime = []
sentKeys = []
print "This will take about " + str(items[0][0] + 1) + " seconds.."
print ""
raw_input("Are you sure the above addresses are correct? [ENTER] to continue ")
print ""
bar = IncrementalBar('Sending', max=(items[0][0]+1))
for i in range(0, items[0][0]+1):
	time.sleep(0.1)
	timeLapsed = timeLapsed + 1
	bar.next()
	if i in publicKeys:
		sentTo = str(publicKeys.get(i , "value"))
		sentKeys.append(sentTo)
		sentTime.append(getTimeStamp())
		if int(items[0][0]+1) == int(addresses):
			bar.finish()
			break

# Transactional report
print ""
print "FINISHED"
print getTimeStamp()
print ""
print 'Payments sent to :'
for i in range(0, int(addresses)):
	print sentKeys[i] + " at " + sentTime[i]
print ""
