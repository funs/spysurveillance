#coding=utf-8
#test 網頁登入
from bs4 import BeautifulSoup
import lxml
import requests

a='NETSurveillance WEB'
url = 'http://114.32.2.167' #114.32.43.1；114.32.3.39
url2 = url+'/Login.htm'
print(url)
print(url2)


data = {'username':'admin','password':''}

headers = { 
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Content-Length':'38',
    'Content-Type':'application/x-www-form-urlencoded',
}



session = requests.Session()
response =session.post(url,headers=headers,data=data,timeout=15)

soup = BeautifulSoup(response.text,'lxml')
#print(soup)
title = soup.select('title')[0].text

print(title)

if title == a:
    print('yes')
else:
    print('no')
