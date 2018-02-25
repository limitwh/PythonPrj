__author__ = 'limitwh'
#coding=utf-8
from bs4 import BeautifulSoup
import requests
import pymysql
import json
import time
import re
def GetItemFromUrl(url):
	Regres=re.compile(r"item.jd.com.*?html")
	PriceID=re.compile(r"\d+")
	htmlstr=requests.get(url).text
	soup = BeautifulSoup(htmlstr,"lxml")
	tagstr = str(soup.find_all(name='ul',attrs={"class":"gl-warp clearfix"})[0])
	TempUrlLists=Regres.findall(tagstr)
	PriceIDList=PriceID.findall(''.join(TempUrlLists))
	TempList=[]
	for x in TempUrlLists:
		TempList.append("https://"+x)
	TempDic=dict(zip(PriceIDList,TempList))
	return TempDic

def GetPrice(itemid,ipoor):
	PriceUrl="https://p.3.cn/prices/mgets?skuIds=J_"+itemid
	Price=requests.get(PriceUrl).json()
	return Price[0]['op']

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

def GetName(url):
	htmlstr=requests.get(url).text
	soup=BeautifulSoup(htmlstr,"lxml")
	divtitle=soup.find_all(name='div',attrs={"class":"item ellipsis"})
	return divtitle[0].text

def InsertDB(ItemList):
	conn=pymysql.connect(host="localhost",user="pytest",password="password",db="JDdb",port=3306,charset='utf8')
	InsterSql="INSERT INTO CURRENT (CurItemId,URL,ItemName,CurPrice) VALUES (%s,%s,%s,%s)"
	cur = conn.cursor() 
	count=0
	try:  
		for Item in ItemList:
			cur.execute(InsterSql,(Item))
			count=count+1
		conn.commit()
	except Exception as e:  
		conn.rollback()
		raise e     
	finally:  
		cur.close()
		conn.close()
	print("Inster %d records into table"%count)

def GetIPoor():
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
	return results

def ClearZero()
	conn=pymysql.connect(host="localhost",user="pytest",password="password",db="JDdb",port=3306,charset='utf8')
	price=0
	itemid=0
	count=0
	Sreachsql="SELECT CURITEMID FROM CURRENT WHERE CURPRICE=0"
	cur = conn.cursor()
	cur.execute(Sreachsql)
	results = cur.fetchall()
	if len(results) == 0:
		print("No records price is zero")
	else:
		print("Totle %d records price is zero"%len(results))
		try:
			for itemid in results:
				price=GetMobPrice(itemid[0])
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
	return count

ItemUrl=GetItemFromUrl("https://list.jd.com/list.html?cat=9987,653,655&page=4")
ItemList=[]
for ItemID in ItemUrl:
	time.sleep(0.15)
	ItemName=(GetName(ItemUrl[ItemID]))
	ItemPrice=(GetMobPrice(ItemID))
	ItemList.append([ItemID,ItemUrl[ItemID],ItemName,ItemPrice])

InsertDB(ItemList)