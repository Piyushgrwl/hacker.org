'''

Question URL: http://www.hacker.org/challenge/chal.php?id=20
Answer URL: http://www.hacker.org/challenge/chal.php?answer=madreup&id=20&go=Submit

Hint: Check Network -> Response Headers for http://www.hacker.org/challenge/misc/one.php

'''

import sys
sys.path.append('../')
import hacker_session as hs

id = 20
answer = "madreup"

hs.hackerSession(answer, id)