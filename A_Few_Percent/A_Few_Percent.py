'''

Question URL: http://www.hacker.org/challenge/chal.php?id=24
Answer URL: http://www.hacker.org/challenge/chal.php?answer=fugly&id=24&go=Submit

'''

import sys
sys.path.append('../')
import hacker_session as hs

id = 24
encrypted_string = "%66%75%67%6C%79"
answer = ""

for i in range(0, len(encrypted_string), 3):
	answer += chr(int(encrypted_string[i+1:i+3], 16))
print(answer)

hs.hackerSession(answer, id)