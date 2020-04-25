'''

Question URL: http://www.hacker.org/challenge/chal.php?id=13
Answer URL: http://www.hacker.org/challenge/chal.php?answer=flippit&id=13&go=Submit

Hint: This is a MD5 encrypted Hash. Use https://www.md5online.org/md5-decrypt.html to decrypt.

'''

import sys
sys.path.append('../')
import hacker_session as hs

id = 13
encrypted_string = "16b87ecc17e3568c83d2d55d8c0d7260"
decrypted_string = "flippit"
answer = decrypted_string
print(answer)

hs.hackerSession(answer, id)