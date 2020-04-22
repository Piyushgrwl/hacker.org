'''

Question URL: http://www.hacker.org/challenge/chal.php?id=2
Answer URL: http://www.hacker.org/challenge/chal.php?answer=61&id=2&go=Submit

'''

import sys
sys.path.append('../')
import hacker_session as hs

id = 2
answer = 17 ^ 39 ^ 11
print(answer)

hs.hackerSession(answer, id)