import requests
import json
import random
import sys
import time
##  get data from website
response = requests.get('https://jsonplaceholder.typicode.com/users')
response = str(response.text)

allPerson = json.loads(response)
maxLenghtName = 0
maxLenghtEmail = 0

for person in allPerson:
	curentChar = len(person["name"])
	if maxLenghtName < curentChar:
		maxLenghtName = curentChar

for person in allPerson:
	curentChar = len(person["email"])
	if maxLenghtEmail < curentChar:
		maxLenghtEmail = curentChar

print("\tName \t\t\t\t" + "Email\t\t" + "Random number")

try:
	delayToExec = int(sys.argv[1])
	time.sleep(delayToExec)
except Exception:
	pass

for person in allPerson:
	countName = len(person["name"])
	countEmail = len(person["email"])
	name = person["name"]
	email = person["email"]
	addSpaceName = maxLenghtName - countName
	addSpaceEmail = maxLenghtEmail - countEmail

	while countName < maxLenghtName:
		name = name + " "
		countName = countName + 1

	while countEmail < maxLenghtEmail:
		email = email + " "
		countEmail = countEmail + 1

	print(name + " | " + email + " | " + str(random.randint(1,3)) + " |")