__author__ = 'limitwh'
#coding=utf-8
from bs4 import BeautifulSoup
import requests
import pymysql
import time
import re

def GetMobPrice(itemid):
	MobPriceUrl="https://item.m.jd.com/product/"+itemid+".html"
	htmlstr=requests.get(MobPriceUrl).text
	soup = BeautifulSoup(htmlstr,"lxml")
	price=0
	time.sleep(0.45)
	try:
		pricetag = soup.find_all(name='input',attrs={"name":"jdPrice"})[0].attrs
		price=pricetag['value']
	except IndexError:
		try:
			bigprice=soup.find_all(name='span',attrs={"class":"big-price"})[0].text
			smallsprice=soup.find_all(name='span',attrs={"class":"small-price"})[0].text
			price=bigprice+smallsprice
		except Exception as e:
			raise e
	finally:
		return price

conn=pymysql.connect(host="localhost",user="pytest",password="password",db="JDdb",port=3306,charset='utf8')
price=0
itemid=0
count=0
Sreachsql="SELECT CURITEMID FROM CURRENT WHERE CURPRICE=0"
cur = conn.cursor()
cur.execute(Sreachsql)
results = cur.fetchall()
print("Totle %d records price is zero"%len(results))
try:
	for itemid in results:
		price=GetMobPrice(itemid[0])
#		print("UPDATE CURRENT SET CURPRICE="+str(price)+" WHERE CURITEMID="+itemid[0])
		cur.execute("UPDATE CURRENT SET CURPRICE="+str(price)+" WHERE CURITEMID="+itemid[0])
		count=count+1
	conn.commit()
except Exception as e:  
	conn.rollback()
	raise e     
finally:  
	cur.close()
	conn.close()
print("Update %d records into table"%count)