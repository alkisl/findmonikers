import string
import random


for k in range(0,4):
	lst = ("a" + random.choice(string.ascii_lowercase) + random.choice('aeiou') for n in xrange(2))
	str = "".join(lst)
	print str
	with open("test.txt", "a") as myfile:
		myfile.write(str + "\n")

with open("test.txt", "a") as myfile:
	myfile.write("\n")