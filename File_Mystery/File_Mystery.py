'''

Question URL: http://www.hacker.org/challenge/chal.php?id=18
Answer URL: http://www.hacker.org/challenge/chal.php?answer=whattogivemysister&id=18&go=Submit

Hint: The data is encoded in GZIP format.

'''

import sys
import zlib
sys.path.append('../')
import hacker_session as hs

id = 18

bytes = []
FileObj = open("fl.bin", "rb")
decompressed_data=zlib.decompress(FileObj.read(), 16+zlib.MAX_WBITS)
answer = str(decompressed_data)
print(answer[2:len(answer)-3])

hs.hackerSession(answer[2:len(answer)-3], id)