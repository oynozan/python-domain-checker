import socket
from colorama import init, Fore
from itertools import permutations

init() #Colorama library initialization

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "w", "v", "y", "z"]
tlds = [".io"]
tldCounter = 0
domainLength = int(input("Enter the domain length > "))

socket.setdefaulttimeout(5)

while True:

	#Get permutation of letters
	possibleDomains = list(permutations(letters, domainLength))

	for domain in possibleDomains:

		primitiveDomain = domain

		#Convert tuple to string
		domain_str = ""
		for i in domain:
			domain_str += i
		domain = domain_str + tlds[tldCounter]

		try:
			socket.gethostbyname(domain)
		except:
			print(Fore.GREEN + "{} is available".format(domain))
		else:
			print(Fore.RED + "{} is not available".format(domain))

		#Last item of list
		if primitiveDomain == possibleDomains[-1]:
			tldCounter += 1
			if tldCounter == tlds.length - 1:
				tldCounter = 0
				domainLength += 1

	#Check domain letter counts up to 6
	if domainLength == 7:
		break