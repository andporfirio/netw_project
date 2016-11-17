def cas_auth():
	import requests
	cas = 'https://systems-login.locaweb.com.br/v1/tickets'
	tgt = requests.post(cas,data={"username": "sistema.closedloop", 
								  "password": "G7GoL213"})
	st = requests.post(tgt.headers.get("Location"),data={"service":
									   "http://cegonha.locaweb.com.br"})
	print (st.content)

	vlans = requests.get("http://cegonha.locaweb.com.br/vlans/")	

	print(vlans)

cas_auth


def cas_auth():
	import requests
	cas = 'https://login.locaweb.com.br/v1/tickets'
	tgt = requests.post(cas,data={"username": "anderson.porfirio", 
								  "password": "LUluLAla42%!*@"})
	st = requests.post(tgt.headers.get("Location"),data={"service":
									   "http://cegonha.locaweb.com.br"})
	print (st.content)

	group = requests.get("http://cegonha.locaweb.com.br/groups/42.json?ticket=%s" %st.content)

	print (group.headers)
cas_auth()