#coding=utf-8
#掃描整個網域的ip狀況，產出掃描結果存在ipwebscan_output.txt中

import datetime
import requests
from bs4 import BeautifulSoup
import lxml

def subnetScan2(subnet2,subnet3):
	a='NETSurveillance WEB'
	b=''
	
	#subnet2 = 32
	#subnet3 = 0

	
	count = 1
	iptitlelist = []
	
	for ip in range(1,256,1):
		try:
			
			url = 'http://114.'+str(subnet2)+'.'+str(subnet3)+'.'+str(ip)+'/'
			#print(url)
			res = requests.get(url,timeout=0.2)
			soup = BeautifulSoup(res.text,'lxml')
			title = soup.select('title')[0].text
			
			iptitle = url+' '+title
			iptitle = iptitle.encode('utf-8')
			print(iptitle)
			iptitlelist.append(iptitle)
		except:
			#b='o'
			'do nothing'
			
	#print('done for '+subnet+' subnet: '+ str(count) +' IPs')
	#print(iplist)
	
	print('done for '+str(subnet3)+' subnet')
	now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	with open('ipwebscan_output.txt','a') as fp:
	    fp.write('\n'.join(iptitlelist))
	    fp.write('\n\ndone for '+str(subnet3)+' subnet')
	    fp.write('\n'+now+'\n\n')
	    

    
if __name__ == '__main__':
	print('start')
	subnetScan2(32,1)
