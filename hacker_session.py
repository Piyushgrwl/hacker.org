import requests

login_data = {
	'username' : 'USERNAME',
	'password' : 'PASSWORD',
	'redirect' : '',
	'login'	: 'Log in'
}

Login_URL = "http://www.hacker.org/forum/login.php"
Base_URL = "http://www.hacker.org/challenge/chal.php"

answer_data = {
	'go' : 'Submit'
}

def hackerSession(var_answer, var_id):
	with requests.Session() as session:
		session_obj = session.post(Login_URL, data = login_data)
		
		answer_data['answer'] = var_answer
		answer_data['id'] = var_id
		
		if var_id == 38:
			answer_response = session.post(Base_URL, headers={'referer': "http://whitehouse.gov"}, params = answer_data)
		else:
			answer_response = session.post(Base_URL, params = answer_data)
		
		if str(answer_response.content).find(" is correct.") != -1:
			print("Success")
		else:
			print("Faiure")
		print('\n' + Base_URL + "?answer=" + str(var_answer) + "&id=" + str(var_id) + "&go=Submit")