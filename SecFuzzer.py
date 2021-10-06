#Changing the Description of this tool won't made you the coder ^_^ !
#Respect Coderz ^_^ 



import urllib.request
import requests
import random
import time
import sys
import os
os.system('clear')
print('''
        !!!!!!   !!!!!!!   !!!!!!!  !!!!!!!!  !!!!!!!!             !!    !!  !!!!!!!!  !!    !!
        !!       !!   !!   !!   !!  !!    !!  !!    !!             !!    !!  !!    !!  !!    !!
        !!!!!!   !!!!!!!   !!!!!!!  !!    !!  !!!!!!!!   !!!!!     !!!!!!!!  !!    !!  !!!!!!!!
        !!       !! !!     !! !!    !!    !!  !! !!                      !!  !!    !!        !!
        !!!!!!   !!  !!    !!  !!   !!!!!!!!  !!  !!                     !!  !!!!!!!!        !!
''')
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 100)
slowprint("[!] Starting : ")
time.sleep(1)
os.system('clear')
print('''
\u001b[1;93m
 ____                  _____                                   
/ ___|    ___    ___  |  ___|  _   _   ____  ____   ___   _ __ 
\___ \   / _ \  / __| | |_    | | | | |_  / |_  /  / _ \ | '__|
 ___) | |  __/ | (__  |  _|   | |_| |  / /   / /  |  __/ | |   
|____/   \___|  \___| |_|      \__,_| /___| /___|  \___| |_|   
                                                               3rr0r-404 | fb: @robin2123.py 
''')


url = input("\033[92m [!] Enter URL : ")
wordlist = input("\033[92m[!] Enter wordlists : ")



def write(word):
	f1 = open("write1.txt","a")
	f1.write(word +"\n")
	
fo = open(wordlist,"r+")
for i in range(2000):
	word = fo.readline(10).strip()
	surl = url+word
	#print (surl)
	
	response = requests.get(surl)
	#print (response)
	if (response.status_code == 200,403):
		print ("\033[91m[!] Found---> ",surl)
		write(word)

