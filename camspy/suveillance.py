#coding=utf-8
#掃描整個網域，並比較是否有目標網頁名稱，將之存在output-XX.txt中
import datetime
import requests
from bs4 import BeautifulSoup
import lxml

a='NETSurveillance WEB'
b=''
subnet = 1
subnet = str(subnet)

count = 1
iplist = []

for ip in range(1,256,1):
	try:
		
		url = 'http://114.32.'+subnet+'.'+str(ip)+'/'
		#print(url)
		res = requests.get(url,timeout=0.2)
		soup = BeautifulSoup(res.text,'lxml')
		title = soup.select('title')[0].text
	
		if a==title:
			#print(url+'Login.htm')
			urllogin = url+'Login.htm'
			print(urllogin)
			#count =count+1
			iplist.append(urllogin)
		else:
			'do nothing'
	except:
		#b='o'
		'do nothing'
		
#print('done for '+subnet+' subnet: '+ str(count) +' IPs')
#print(iplist)

print('done for '+subnet+' subnet: '+ str(len(iplist)) +' IPs')
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open('output-'+subnet+'.txt', 'w') as fp:
    fp.write('\n'.join(iplist))
    fp.write('\n\ndone for '+subnet+' subnet: '+ str(len(iplist)) +' IPs')
    fp.write('\n\n'+now)
