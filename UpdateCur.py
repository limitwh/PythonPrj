__author__ = 'limitwh'
#coding=utf-8
from bs4 import BeautifulSoup
import requests
import pymysql
import time
import re

Item0List=[['11867146203', 'https://item.jd.com/11867146203.html', '小米（MI）红米4A', 0], ['24820328818', 'https://item.jd.com/24820328818.html', 'vivo Y75 全面屏手机 4GB+64GB 移动联通电信4G手机 双卡双待 玫瑰金', 0], 
 ['11794447957', 'https://item.jd.com/11794447957.html', 'AppleiPhone X', '7958.00'], ['21679736921', 'https://item.jd.com/21679736921.html', '小米（MI） 红米5 Plus 手机 全面屏 金色 全网通(4G+64G)', '1299.00'], 
 ['13038157255', 'https://item.jd.com/13038157255.html', '华为（HUAWEI） 荣耀畅玩6A 全网通4G智能手机 金色 3G+32G', 0], ['11404871391', 'https://item.jd.com/11404871391.html', 'AppleiPhone6', 0], 
 ['6072102', 'https://item.jd.com/6072102.html', '华为荣耀9青春版', 0], ['11167077801', 'https://item.jd.com/11167077801.html', 'OPPOA57', 0], ['18608306444', 'https://item.jd.com/18608306444.html', 'AppleiPhone6', '2258.00'], 
 ['20887332355', 'https://item.jd.com/20887332355.html', 'vivo X20王者荣耀限量版 全面屏 全网通 6GB+64GB 移动联通电信4G手机', 0], ['5570999', 'https://item.jd.com/5570999.html', '锤子坚果 Pro 2', 0], 
 ['13734536642', 'https://item.jd.com/13734536642.html', '华为（HUAWEI）畅享7', 0], ['22225126641', 'https://item.jd.com/22225126641.html', 'vivo X20新年限量礼盒 4GB+64GB 全面屏双摄 移动联通电信4G手机 磨砂黑', 0], 
 ['16580586466', 'https://item.jd.com/16580586466.html', 'AppleiPhone 8 Plus', '6458.00'], ['10777694789', 'https://item.jd.com/10777694789.html', '魅族（MEIZU） 魅蓝Note5 手机 月光银 （3G+32G）标配', '758.00'], 
 ['20813342268', 'https://item.jd.com/20813342268.html', '魅族（MEIZU） 魅蓝Note5 移动定制全网通4G手机 银色 3G+32G', '699.00'], ['18793230655', 'https://item.jd.com/18793230655.html', 'Apple 苹果 iPhone X 手机 全面屏 深空灰色 64GB', '7888.00'], 
 ['16579983415', 'https://item.jd.com/16579983415.html', 'AppleiPhone X', '9038.00'], ['15616497820', 'https://item.jd.com/15616497820.html', '魅族（MEIZU）魅蓝 Note6', 0], 
 ['18108508070', 'https://item.jd.com/18108508070.html', 'vivo Y79 全面屏手机 4GB+64GB 移动联通电信4G手机 双卡双待 磨砂黑', '1998.00'],
 ['22320392453', 'https://item.jd.com/22320392453.html', '小米小米Note3', 0], ['5437633', 'https://item.jd.com/5437633.html', 'vivoX20', '3498.00'], 
 ['19287824497', 'https://item.jd.com/19287824497.html', '小米（MI）小米5X', 0], ['10833486405', 'https://item.jd.com/10833486405.html', '华为（HUAWEI） 荣耀6X 畅玩6X 手机 冰河银 全网通(3GB+32GB)公开版', 0], 
 ['5531853', 'https://item.jd.com/5531853.html', 'AppleiPhone X', '8388.00'], ['20533811681', 'https://item.jd.com/20533811681.html', 'vivo Y66i 全网通 3GB+32GB 移动联通电信4G手机 双卡双待 玫瑰金', '1198.00'],
 ['20904886128', 'https://item.jd.com/20904886128.html', '华为（HUAWEI）荣耀V10', '3099.00'], ['4747522', 'https://item.jd.com/4747522.html', 'vivoY55', 0], 
 ['12260682497', 'https://item.jd.com/12260682497.html', '华为（HUAWEI）P10', 0], ['5835407', 'https://item.jd.com/5835407.html', 'vivoY66i', '1198.00'], 
 ['19994179320', 'https://item.jd.com/19994179320.html', '华为（HUAWEI）Mate 10 Pro', '5399.00'], ['11464031106', 'https://item.jd.com/11464031106.html', 'AppleiPhone5s', '1420.00'],
 ['13444833474', 'https://item.jd.com/13444833474.html', '华为（HUAWEI）畅享6S', 0], ['17215885416', 'https://item.jd.com/17215885416.html', '华为（HUAWEI） 华为Mate10 手机 亮黑色 全网通(4GB+64GB)标准版', 0],
 ['5832725', 'https://item.jd.com/5832725.html', 'vivoY66i', 0], ['21056257663', 'https://item.jd.com/21056257663.html', 'HUAWEI荣耀V10', 0], ['12857064004', 'https://item.jd.com/12857064004.html', '小米（MI）小米6', 0], 
 ['5179864', 'https://item.jd.com/5179864.html', '诺基亚3310', '399.00'], ['14507356150', 'https://item.jd.com/14507356150.html', '华为（HUAWEI）畅享6', 0], ['4436773', 'https://item.jd.com/4436773.html', '魅族魅蓝A5', 0], 
 ['10492297255', 'https://item.jd.com/10492297255.html', '华为（HUAWEI） 荣耀8 双卡双待4G手机 魅海蓝 全网通(4+64G) 顶配', 0], 
 ['22227700692', 'https://item.jd.com/22227700692.html', 'vivo X20Plus新年限量礼盒 4GB+64GB 移动联通电信4G手机 磨砂黑', '3298.00'],
 ['12553694715', 'https://item.jd.com/12553694715.html', '小米（MI） 小米 红米4A 2+16GB 深空灰 全网通版', '539.00'], 
 ['18614205208', 'https://item.jd.com/18614205208.html', 'Apple 苹果 iPhoneX (A1865)  手机 银色 全网通 64GB', '7836.00'],
 ['11463828713', 'https://item.jd.com/11463828713.html', 'Apple 苹果6  iPhone 6 手机 金色 全网通(32G ROM)', 0], ['12592003625', 'https://item.jd.com/12592003625.html', 'vivo Y53  全网通 2GB+16GB 移动联通电信4G手机 双卡双待 金色', '899.00'], 
 ['15610845217', 'https://item.jd.com/15610845217.html', '魅族（MEIZU）魅蓝 Note6', '1499.00'], ['12177654563', 'https://item.jd.com/12177654563.html', '魅族（MEIZU）魅蓝E2', '765.00'],
 ['15638133669', 'https://item.jd.com/15638133669.html', '魅族（MEIZU） 魅族 魅蓝Note6 手机 香槟金 全网通(4G RAM+64G ROM)【尊享版】', '1499.00'],
 ['18726688989', 'https://item.jd.com/18726688989.html', '小米（MI）小米5X', '1309.00'], ['15501730722', 'https://item.jd.com/15501730722.html', 'AppleiPhone X', 0],
 ['4136731', 'https://item.jd.com/4136731.html', '酷派5267', '299.00'], ['16555705767', 'https://item.jd.com/16555705767.html', 'Apple 苹果 iPhone X手机 深空灰色 256G', 0],
 ['17760675843', 'https://item.jd.com/17760675843.html', '华为（HUAWEI） 荣耀V9 全网通 移动联通电信4G双卡双待 智能手机 幻夜黑 全网通(6G+128G)', '3499.00'],
 ['17301293311', 'https://item.jd.com/17301293311.html', '华为（HUAWEI）6X', 0], ['11789883614', 'https://item.jd.com/11789883614.html', '小米（MI）5A', 0], 
 ['17698485993', 'https://item.jd.com/17698485993.html', 'vivo X20 全面屏手机 全网通 4GB+128GB 移动联通电信4G手机 黑金 旗舰版', '3398.00'], ['5911245', 'https://item.jd.com/5911245.html', '360N6 Lite', 0], 
 ['20979546431', 'https://item.jd.com/20979546431.html', 'vivo X20 全面屏手机 全网通 4GB+64GB 移动联通电信4G手机 星耀红限量礼盒 标准版', 0], ['25388860570', 'https://item.jd.com/25388860570.html', '魅族（MEIZU）魅蓝S6', 0]]

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

def ClearZeroList(itemlist):
	count=0
	for Item in itemlist:
		if(Item[3]==0):
			count=count+1
			Tempprice=GetMobPrice(Item[0])
			Item[3]=Tempprice
	return count,itemlist

lists=ClearZeroList(Item0List)
print(lists[0])