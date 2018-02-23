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

def GetPrice(itemid):
	PriceUrl = "https://p.3.cn/prices/mgets?skuIds=J_"+itemid
	Price=requests.get(PriceUrl).json()
	return Price[0]['op']

def GetName(url):
	htmlstr=requests.get(url).text
	soup = BeautifulSoup(htmlstr,"lxml")
	divtitle = soup.find_all(name='div',attrs={"class":"item ellipsis"})
	return divtitle[0].text

def InsertDB(list):
	DB=pymysql.connect(host="localhost",user="pytest",password="password",db="JDdb",port=3306,charset='utf8')
	curs = DB.cursor()
	push=0
	


ItemUrl = GetItemFromUrl("https://list.jd.com/list.html?cat=9987,653,655&page=3")
ItemList=[]
for ItemID in ItemUrl:
	ItemName=(GetName(ItemUrl[ItemID]))
	time.sleep(0.3)
	ItemPrice=(GetPrice(ItemID))
	time.sleep(0.3)
	ItemList.append([ItemID,ItemUrl[ItemID],ItemName,ItemPrice])

print(ItemList)