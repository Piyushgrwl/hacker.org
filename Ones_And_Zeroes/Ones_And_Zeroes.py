'''

Question URL: http://www.hacker.org/challenge/chal.php?id=29
Answer URL: http://www.hacker.org/challenge/chal.php?answer=wednesday&id=29&go=Submit

Hint: Convert Binary into ASCII.

'''

import sys
import binascii
sys.path.append('../')
import hacker_session as hs

id = 29
encrypted_string = "01110101 01110011 01100101 00100000 01110111 01100101 01100100 01101110 01100101 01110011 01100100 01100001 01111001 00100000 01100110 01101111 01110010 00100000 01110100 01101000 01100101 00100000 01100001 01101110 01110011 01110111 01100101 01110010"
decrypted_string = ""

var1 = encrypted_string.split(' ')
for item in var1:
	var2 = int(item, 2)
	decrypted_string += binascii.unhexlify('%x' % var2)

print(decrypted_string)
#Decrypted String is "use wednesday for the answer"

hs.hackerSession("wednesday", id)