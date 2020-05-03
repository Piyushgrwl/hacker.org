'''

Question URL: http://www.hacker.org/challenge/chal.php?id=27
Answer URL: http://www.hacker.org/challenge/chal.php?answer=marmelade&id=27&go=Submit

'''

import sys
sys.path.append('../')
import hacker_session as hs

id = 27
answer = "marmelade"

hs.hackerSession(answer, id)