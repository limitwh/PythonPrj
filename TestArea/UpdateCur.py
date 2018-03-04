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

def ClearZeroList(item0list):
	count=0
	for Item in item0list:
		if(Item[1]==0):
			count=count+1
			Tempprice=GetMobPrice(Item[0])
			Item[1]=Tempprice
	return count,item0list

def ClearZeroPrice(item0list):
	lists=ClearZeroList(item0list)
	while (lists[0] !=0):
		print("Totle %d records price is zero"%lists[0])
		lists=ClearZeroList(lists[1])
	return lists[1]

def UpdateCur():
	conn=pymysql.connect(host="localhost",user="pytest",password="password",db="JDdb",port=3306,charset='utf8')
	Sreachsql="SELECT CurItemId FROM CURRENT"
	cur = conn.cursor()
	Item0List=[]
	count=0
	try:  
		cur.execute(Sreachsql)
		results = cur.fetchall()
	except Exception as e:  
		conn.rollback()
		raise e     
	finally:  
		cur.close()
	for ItemID in results:
		price=GetMobPrice(ItemID[0])
		Item0List.append([ItemID[0],price])
	Item0List=ClearZeroPrice(Item0List)
	cur = conn.cursor()
	try:
		for Item in Item0List:
			price=GetMobPrice(Item[0])
			if(price!=""):
				cur.execute("UPDATE CURRENT SET CURPRICE="+str(Item[1])+" WHERE CURITEMID="+str(Item[0]))
				count=count+1
		conn.commit()
	except Exception as e:  
		conn.rollback()
		raise e     
	finally:  
		cur.close()
		conn.close()
	return count

print(UpdateCur())