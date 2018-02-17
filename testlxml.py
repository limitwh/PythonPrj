__author__ = 'limitwh'
#coding=utf-8
import requests
from lxml import etree

Url="https://item.jd.com/3888216.html"
UrlStr=requests.get(Url).content
html=etree.HTML(UrlStr)
print(UrlStr.decode('unicode_escape'))
#tree = etree.parse(UrlStr)
#r = tree.XPath("/html/body/div[11]/div[2]/div[1]/div[2]/div[1]/div[1]/ul[3]/li[1]")
#print(len(r))