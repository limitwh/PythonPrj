__author__ = 'limitwh'
#coding=utf-8
import requests
from bs4 import BeautifulSoup
MobPriceUrl="https://item.m.jd.com/product/5996385.html"
htmlstr=requests.get(MobPriceUrl).text
soup = BeautifulSoup(htmlstr,"lxml")
price=0
print(htmlstr)
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
	print(price)