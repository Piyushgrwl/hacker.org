'''

Question URL: http://www.hacker.org/challenge/chal.php?id=19
Answer URL: http://www.hacker.org/challenge/chal.php?answer=4092&id=19&go=Submit

'''

import sys
sys.path.append('../')
import hacker_session as hs

id = 19
fib = {}
fib[0] = fib[1] = 1
answer = 0

for i in range(2, 18):
	fib[i] = fib[i-1] + fib[i-2]

for i in range(9, 17):
	answer += fib[i]
print(answer)

hs.hackerSession(answer, id)