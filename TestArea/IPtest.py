__author__ = 'limitwh'
#coding=utf-8
import requests
import json
from bs4 import BeautifulSoup
import pymysql

conn=pymysql.connect(host="localhost",user="pytest",password="password",db="JDdb",port=3306,charset='utf8')
GetIP="SELECT HTTP,IPURL FROM IPOOR"
cur = conn.cursor() 
try:  
	cur.execute(GetIP)
	results = cur.fetchall()
except Exception as e:  
	conn.rollback()
	raise e     
finally:  
	cur.close()
	conn.close()


IPdict=dict((y, x) for x, y in results)
TestUrl = "http://ip.chinaz.com/"
iproxy={}
count=0
for HTTP in IPdict:
	iproxy={HTTP:IPdict[HTTP]}
	IPtest=requests.get(TestUrl,proxies=iproxy).text
	soup=BeautifulSoup(IPtest,"lxml")
	ip=soup.find_all(name='p',attrs={"class":"getlist pl10"})
	print(iproxy)
	print(ip[0].text)
	iproxy.clear()