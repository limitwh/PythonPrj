__author__ = 'limitwh'
#coding=utf-8
import requests
from bs4 import BeautifulSoup
Url="https://item.jd.com/4230887.html"
UrlDict={'5936828': 'https://item.m.jd.com/product/5936828.html'}
for key in UrlDict:
	htmlstr=requests.get(UrlDict[key]).text
	soup = BeautifulSoup(htmlstr,"lxml")
	pricetag = soup.find_all(name='input',attrs={"name":"jdPrice"})[0].attrs
	print(pricetag)
#for key in UrlDict:
#	time.sleep(1.5)
#	print(key+':'+UrlDict[key])