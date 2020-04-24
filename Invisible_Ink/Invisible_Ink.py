'''

Question URL: http://www.hacker.org/challenge/chal.php?id=11
Answer URL: http://www.hacker.org/challenge/chal.php?answer=blind&id=11&go=Submit

Hint: Check the source code.

'''

import sys
sys.path.append('../')
import hacker_session as hs

id = 11
answer = "blind"

hs.hackerSession(answer, id)