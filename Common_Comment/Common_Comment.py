'''

Question URL: http://www.hacker.org/challenge/chal.php?id=3
Answer URL: http://www.hacker.org/challenge/chal.php?answer=veritas&id=3&go=Submit

Hint: Check the source code.

'''

import sys
sys.path.append('../')
import hacker_session as hs

id = 3
answer = "veritas"

hs.hackerSession(answer, id)