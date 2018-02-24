__author__ = 'limitwh'
#coding=utf-8
from bs4 import BeautifulSoup
import requests
import pymysql
import json
import time
import re
def GetItemFromUrl(url):
	Urlres=requests.get(url)
	Regres=re.compile(r"item.jd.com.*?html")
	PriceID=re.compile(r"\d+")
	TempUrlLists=Regres.findall(str(Urlres.content,'utf-8'))
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

def GetName(url):
	htmlstr=requests.get(url).text
	soup=BeautifulSoup(htmlstr,"lxml")
	divtitle=soup.find_all(name='div',attrs={"class":"item ellipsis"})
	return divtitle[0].text

def InsertDB(ItemList):
	conn=pymysql.connect(host="localhost",user="pytest",password="password",db="JDdb",port=3306,charset='utf8')
	GetIP="INSERT INTO CURRENT (CurItemId,URL,ItemName,CurPrice) VALUES (%s,%s,%s,%s)"
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


ItemUrl=GetItemFromUrl("https://list.jd.com/list.html?cat=9987,653,655&page=3")
ItemList=[]
#or ItemID in ItemUrl:
#	ItemName=(GetName(ItemUrl[ItemID]))
#	time.sleep(0.3)
#	ItemPrice=(GetPrice(ItemID))
#	time.sleep(0.3)
#	ItemList.append([ItemID,ItemUrl[ItemID],ItemName,ItemPrice])

IPoor=GetIPoor()
print(IPoor)