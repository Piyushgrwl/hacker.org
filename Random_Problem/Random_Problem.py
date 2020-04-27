'''

Question URL: http://www.hacker.org/challenge/chal.php?id=15
Answer URL: http://www.hacker.org/challenge/chal.php?answer=-2147483648&id=15&go=Submit

Hint: In JAVA, int is limited from -2,147,483,648 to 2,147,483, 647 i.e; of 4 bytes.

'''

import sys
sys.path.append('../')
import hacker_session as hs

id = 15
answer = -2147483648

'''
public int bucketFromRandom(int randomNumber) {
	int a[]	= new int[10];
	for (int i = 0; i < a.length; i++)
		a[i] = i * randomNumber;
	int index = Math.abs(randomNumber) % a.length;
	return a[index];
}
'''

hs.hackerSession(answer, id)