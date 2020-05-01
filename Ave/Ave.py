'''

Question URL: http://www.hacker.org/challenge/chal.php?id=23
Answer URL: http://www.hacker.org/challenge/chal.php?answer=deadmanschest&id=23&go=Submit

Hint: Caesarian Shift with a Rotaiton of 17.

'''

import sys
sys.path.append('../')
import hacker_session as hs

id = 23
encrypted_string = "cqrb lryqna rb fjh, fjh qjamna cqjw axc cqracnnw. qnan, hxd wnena twxf qxf oja cx bqroc! xq kh cqn fjh, cqn jwbfna rb mnjmvjwblqnbc."
decrypted_string = "this cipher is way, way harder than rot thirteen. here, you never know how far to shift! oh by the way, the answer is deadmanschest."
answer = "deadmanschest"

hs.hackerSession(answer, id)