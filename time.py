__author__ = 'limitwh'
#coding=utf-8
import time
#time.struct_time(tm_year=YYYY, tm_mon=MM, tm_mday=DD, tm_hour=HH, tm_min=MM, tm_sec=SS, tm_wday=MM, tm_yday=DDD, tm_isdst=0)
localtime1 = time.localtime(time.time())
#Wed Feb  7 23:46:04 2018
localtime2 = time.asctime( time.localtime(time.time()))
print(localtime1)
print(localtime2)
#2018-02-07 23:47:40
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))