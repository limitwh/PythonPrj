__author__ = 'limitwh'
#coding=utf-8
from bs4 import BeautifulSoup
import requests
import pymysql
import json
import time
import re

#从URL中取得商品ID
def InitGetItemFromUrl(url):
	Regres=re.compile(r"item.jd.com.*?html")
	PriceID=re.compile(r"\d+")
	htmlstr=requests.get(url).text
	soup = BeautifulSoup(htmlstr,"lxml")
	#用正则表达式取得商品陈列标签内的商品ID
	tagstr = str(soup.find_all(name='ul',attrs={"class":"gl-warp clearfix"})[0])
	TempUrlLists=Regres.findall(tagstr)
	PriceIDList=PriceID.findall(''.join(TempUrlLists))
	TempList=[]
	for x in TempUrlLists:
		TempList.append("https://"+x)
	TempDic=dict(zip(PriceIDList,TempList))
	#返回一个字典，格式----{商品ID：该商品的URL}
	return TempDic

#从webservice取得价格
def GetPrice(itemid,ipoor):
	PriceUrl="https://p.3.cn/prices/mgets?skuIds=J_"+itemid
	#webservice返回的是一个json对象
	Price=requests.get(PriceUrl).json()
	return Price[0]['op']

#从移动端网页取得价格
def GetMobPrice(itemid):
	MobPriceUrl="https://item.m.jd.com/product/"+itemid+".html"
	htmlstr=requests.get(MobPriceUrl).text
	soup = BeautifulSoup(htmlstr,"lxml")
	price=0
	time.sleep(0.45)
	#移动端存在两种价格标签
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

#从URL中取得商品名称
def GetName(url):
	htmlstr=requests.get(url).text
	soup=BeautifulSoup(htmlstr,"lxml")
	#商品名称标签
	divtitle=soup.find_all(name='div',attrs={"class":"item ellipsis"})
	return divtitle[0].text

#初始化插入Item到Mysql表中
def InitInsertDB(ItemList):
	conn=pymysql.connect(host="localhost",user="pytest",password="password",db="JDdb",port=3306,charset='utf8')
	InsterSql="INSERT INTO CURRENT (CURITEMID,URL,ITEMNAME,CURPRICE) VALUES (%s,%s,%s,%s)"
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

#取得代理IP，未使用
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

#移动端网页爬取价格时，仍然有0价格的情况，下记函数在初始化插入后对0价格做更新处理
def InitClearZero():
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

#Cur表更新完成之后，下记函数将Cur表中的信息同步到His表中
def UpdateHis():
	conn=pymysql.connect(host="localhost",user="pytest",password="password",db="JDdb",port=3306,charset='utf8')
	Sreachsql="SELECT CURITEMID,CURPRICE,UPDTIMEVERSION FROM CURRENT"
	InsterSql="INSERT INTO HISTORY (HISITEMID,HISPRICE,GETTIMEVERSION) VALUES (%s,%s,%s)"
	cur = conn.cursor() 
	try:  
		cur.execute(Sreachsql)
		results = cur.fetchall()
	except Exception as e:  
		conn.rollback()
		raise e     
	finally:  
		cur.close()
	count=0
	cur = conn.cursor() 
	try:  
		for Item in results:
			cur.execute(InsterSql,(Item))
			count=count+1
		conn.commit()
	except Exception as e:  
		conn.rollback()
		raise e     
	finally:  
		cur.close()
		conn.close()
	print("Inster %d records into History table"%count)

#移动端网页爬取价格时，仍然有0价格的情况，下记函数在日常更新后对0价格做更新处理
def ClearZeroList(item0list):
	count=0
	for Item in item0list:
		if(Item[1]==0):
			count=count+1
			Tempprice=GetMobPrice(Item[0])
			Item[1]=Tempprice
	#返回值中，count是0价格的计数，item0list是本次更新0价格之后的ItemList
	return count,item0list

#移动端网页爬取价格时，仍然有0价格的情况，下记函数在日常更新后对0价格做更新处理
def ClearZeroPrice(item0list):
	lists=ClearZeroList(item0list)
	#反复调用0价格更新处理直至没有0价格
	while (lists[0] !=0):
		print("Totle %d records price is zero"%lists[0])
		lists=ClearZeroList(lists[1])
	return lists[1]

#日常更新Cur表。仍有null price的问题尚未解决，数据中时间戳属性需要改为非自动更新
def UpdateCur():
	#正则表达式：从str中将float筛选出来
	ClearPrice=re.compile(r"^\d+?\.\d+?$")
	conn=pymysql.connect(host="localhost",user="pytest",password="password",db="JDdb",port=3306,charset='utf8')
	Sreachsql="SELECT CURITEMID FROM CURRENT"
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
	for Price in Item0List:
		if (len(ClearPrice.findall(Price[1])) == 0):
			Price[1]='-1'
	cur = conn.cursor()
	print(Item0List)
	try:
		for Item in Item0List:
			price=GetMobPrice(Item[0])
			updatetime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
			cur.execute("UPDATE CURRENT SET CURPRICE="+str(Item[1])+", UPDTIMEVERSION='"+str(updatetime)+"' WHERE CURITEMID="+str(Item[0]))
			count=count+1
		conn.commit()
	except Exception as e:  
		conn.rollback()
		raise e     
	finally:  
		cur.close()
		conn.close()
	print("Totle %d records updated in current"%count)
	return count

#UpdateCur()
UpdateHis()

#ItemUrl=GetItemFromUrl("https://list.jd.com/list.html?cat=9987,653,655&page=4")
#ItemList=[]
#for ItemID in ItemUrl:
#	time.sleep(0.15)
#	ItemName=(GetName(ItemUrl[ItemID]))
#	ItemPrice=(GetMobPrice(ItemID))
#	ItemList.append([ItemID,ItemUrl[ItemID],ItemName,ItemPrice])
#print(ItemList)

#InsertDB(ItemList)