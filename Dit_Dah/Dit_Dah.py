'''

Question URL: http://www.hacker.org/challenge/chal.php?id=28
Answer URL: http://www.hacker.org/challenge/chal.php?answer=hoarse&id=28&go=Submit

Hint: Use Morse Code Converter

'''

import sys
sys.path.append('../')
import hacker_session as hs

id = 28
encrypted_string = "- .... . .- -. ... .-- . .-. .. ... .... --- .- .-. ... ."
decrypted_string = "theanswerishoarse"

hs.hackerSession("hoarse", id)