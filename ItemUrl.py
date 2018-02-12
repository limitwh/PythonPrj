__author__ = 'limitwh'
#coding=utf-8
import requests
import time
Url="https://item.jd.com/3888216.html"
UrlDict={'3888216': 'https://item.jd.com/3888216.html', '4230887':'https://item.jd.com/4230887.html', '5835263': 'https://item.jd.com/5835263.html'}
response=requests.get(Url)
print(response.xpath("/html/body/div[11]/div[2]/div[1]/div[2]/div[1]/div[1]/ul[3]/li[1]"))


#for key in UrlDict:
#	time.sleep(1.5)
#	print(key+':'+UrlDict[key])