'''

Question URL: http://www.hacker.org/challenge/chal.php?id=1
Answer URL: http://www.hacker.org/challenge/chal.php?answer=fishcake&id=1&go=Submit

Hint: Caesarian Shift with a Rotaiton of 13.

'''

import sys
sys.path.append('../')
import hacker_session as hs

id = 1
encrypted_string = "Guvf zrffntr vf rapelcgrq va ebg 13. Lbhe nafjre vf svfupnxr."
decrypted_string = "This message is encrypted in rot 13. Your answer is fishcake."

answer = "fishcake"
hs.hackerSession(answer, id)