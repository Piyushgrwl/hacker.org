'''

Question URL: http://www.hacker.org/challenge/chal.php?id=31
Answer URL: http://www.hacker.org/challenge/chal.php?answer=soundofsilence&id=31&go=Submit

Hint: It's encoded in Braille Coding.

12
34  ==>  Single Character representation of Braille Code
56

'''

import sys
sys.path.append('../')
import hacker_session as hs

id = 31
braille = {
	'.     ' : 'a',
	'. .   ' : 'b',
	'..    ' : 'c',
	'.. .  ' : 'd',
	'.  .  ' : 'e',
	'...   ' : 'f',
	'....  ' : 'g',
	'. ..  ' : 'h',
	' ..   ' : 'i',
	' ...  ' : 'j',
	'.   . ' : 'k',
	'. . . ' : 'l',
	'..  . ' : 'm',
	'.. .. ' : 'n',
	'.  .. ' : 'o',
	'... . ' : 'p',
	'..... ' : 'q',
	'. ... ' : 'r',
	' .. . ' : 's',
	' .... ' : 't',
	'.   ..' : 'u',
	'. . ..' : 'v',
	' ... .' : 'w',
	'..  ..' : 'x',
	'.. ...' : 'y',
	'.  ...' : 'z',
	'  .   ' : ',',
	'  .. .' : '.'
}

encrypted_string = [
	" . .  .     .  ..  .  . .  .      .  .     . .  .  .. .. .  ..  .  . .  .  .. .. .  ",
	".. ..  .        . .  ..  . ..    .  .     .   .     .  .  . .  .  .  .   .  .     . ",
	".              .  .   .    .        .     .  .  .. .     .     .     .     .        "]

decrypted_string = ""

i = 0
while i < len(encrypted_string[1]):
	if encrypted_string[0][i] == ' ' and encrypted_string[1][i] == ' ' and encrypted_string[2][i] == ' ':
		decrypted_string += " "
		i += 1
	else:
		key = encrypted_string[0][i] + encrypted_string[0][i+1] + encrypted_string[1][i] + encrypted_string[1][i+1] + encrypted_string[2][i] + encrypted_string[2][i+1]
		decrypted_string += braille[key]
		i += 2

print(decrypted_string)
#decrypted_string is "t h e    a n s w e r    i s    s o u n d o f s i l e n c e"
answer = "soundofsilence"

hs.hackerSession(answer, id)