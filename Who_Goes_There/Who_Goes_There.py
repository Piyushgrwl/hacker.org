'''

Question URL: http://www.hacker.org/challenge/chal.php?id=17
Answer URL: http://www.hacker.org/challenge/chal.php?answer=lwrghsuyip&id=17&go=Submit

'''

import sys
sys.path.append('../')
import hacker_session as hs

id = 17
username = "piyushgrwl"

hs.hackerSession(username[::-1], id)