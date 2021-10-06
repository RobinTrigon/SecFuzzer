#Changing the Description of this tool won't made you the coder ^_^ !
#Respect Coderz ^_^ 


import urllib.request
import os
import time
import sys
os.system('clear')
print("""
\033[96m
 _____   _   _   _____  _____  _____   ____  
|  ___| | | | | |__  / |__  / | ____| |  _ \ 
| |_    | | | |   / /    / /  |  _|   | |_) |
|  _|   | |_| |  / /_   / /_  | |___  |  _ < 
|_|      \___/  /____| /____| |_____| |_| \__\
                                             
""")


url = input("\033[97m [!] Enter URL # ")
wordlist = input("\033[97m [!] Enter wordlists # ")

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
		print ("[+] found :- ",surl)
		write(word)
	else:	
		print ("[-] Not found :- ",surl)
		pass
