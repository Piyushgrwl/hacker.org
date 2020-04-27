'''

Question URL: http://www.hacker.org/challenge/chal.php?id=16
Answer URL: http://www.hacker.org/challenge/chal.php?answer=kuakua&id=16&go=Submit

Hint: 
1. BIN file header "CA FE BA BE" suggests it's a JAVA CLASS file.
2. Change the file extension to .class and decompile it to get the .java file.

'''

import sys
sys.path.append('../')
import hacker_session as hs

id = 16

def showMeSomethingInteresting():
	c = "axkyue"
	a = 73
	b = 391
	s = ""
	for i in range(6):
		s += c[(i * b + (i + 8) * a) % len(c)]
	print(s)

showMeSomethingInteresting()
answer = "kuakua"
hs.hackerSession(answer, id)