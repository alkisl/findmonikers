import string
import random
for k in range(0,5):
	lst = (random.choice(string.ascii_lowercase) + random.choice('aeiou') for n in xrange(3))
	str = "".join(lst)
	print str