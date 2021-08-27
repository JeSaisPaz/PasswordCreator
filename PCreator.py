import random
import string

charnum = int(input("How many characters in your password ? > "))
strg = ""
acceptedstrings = string.printable[:-5]
for x in range(0, charnum):
	strg += random.choice(acceptedstrings)

print(strg)
