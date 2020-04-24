'''

Question URL: http://www.hacker.org/challenge/chal.php?id=10
Answer URL: http://www.hacker.org/challenge/chal.php?answer=squint&id=10&go=Submit

Hint: Check the source code.

'''

import sys
sys.path.append('../')
import hacker_session as hs

id = 10

answer = "squint"
hs.hackerSession(answer, id)