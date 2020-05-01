'''

Question URL: http://www.hacker.org/challenge/chal.php?id=21
Answer URL: http://www.hacker.org/challenge/chal.php?answer=ADUMBRATE&id=21&go=Submit

Hint: Use https://quipqiup.com

'''

import sys
sys.path.append('../')
import hacker_session as hs

id = 21
encrypted_string = "ISS NVVK DIPXYWA PIT AVSUY QIAOP PWZEHVNWIEDZ. CDYT ZVM LOTK HDY AVSMHOVT HV HDOA HYFH, ZVM COSS QY IQSY HV NYH HDY ITACYW, CDOPD OA IKMGQWIHY."
decrypted_string = "ALL GOOD HACKERS CAN SOLVE BASIC CRYPTOGRAPHY. WHEN YOU FIND THE SOLUTION TO THIS TEXT, YOU WILL BE ABLE TO GET THE ANSWER, WHICH IS ADUMBRATE."

answer = "ADUMBRATE"
hs.hackerSession(answer, id)