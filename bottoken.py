import os, re, requests, bs4
from bs4 import BeautifulSoup as parser
ses=requests.Session()
M = '\x1b[1;91m' # MERAH			
H = '\x1b[1;92m' # HIJAU
N = '\x1b[0m'	# WARNA MATI
freetoken = []
		
def get_token():
	url = parser(ses.get("https://free.facebook.com/100040708001839/posts/716737126359881/?app=fbl").text,"html.parser")
	data = re.findall("EAA\w+",str(url))
	for token in data:
		try:
			if len(token)>=35:
				if token in freetoken:pass
				else:
					freetoken.append(token)
					print(f"""
 [+] Status : {cekstatus(token)}
 [+] Token  : {token}""")
		except:continue

def cekstatus(token):
	try:
		url = ses.get("https://graph.facebook.com/me?access_token={token}").json()
		data = f"{H}Aktif{N}"
	except KeyError:
		data = f"{M}Kadaluwarsa{N}"
	return data
	
if __name__ == '__main__':
	get_token()