'''

Question URL: http://www.hacker.org/challenge/chal.php?id=25
Answer URL: http://www.hacker.org/challenge/chal.php?answer=spaghetti&id=25&go=Submit

'''

import sys
sys.path.append('../')
import hacker_session as hs

id = 25
answer = "spaghetti"

hs.hackerSession(answer, id)