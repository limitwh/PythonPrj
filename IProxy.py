__author__ = 'limitwh'
#coding=utf-8
import pymysql
IPoor=[['1.195.122.97','47482','HTTPS'],
['106.58.120.127','80','HTTP'],
['110.72.19.239','8123','HTTP'],
['110.72.27.189','8123','HTTPS'],
['110.72.33.120','8123','HTTP'],
['110.72.33.18','8123','HTTP'],
['110.73.48.177','8123','HTTPS'],
['110.73.51.15','8123','HTTPS'],
['110.73.51.16','8123','HTTP'],
['110.73.53.0','8123','HTTP'],
['110.73.54.117','8123','HTTP'],
['110.73.9.224','8123','HTTP'],
['110.90.129.93','24496','HTTPS'],
['111.155.116.201','8123','HTTP'],
['111.155.116.211','8123','HTTP'],
['111.155.116.215','8123','HTTP'],
['111.155.116.217','8123','HTTP'],
['111.155.116.226','8123','HTTP'],
['111.155.116.237','8123','HTTP'],
['111.155.116.238','8123','HTTP'],
['111.155.116.240','8123','HTTP'],
['111.155.116.247','8123','HTTP'],
['112.193.208.216','8123','HTTP'],
['112.234.145.153','8118','HTTPS'],
['113.121.242.110','808','HTTP'],
['113.93.102.231','30201','HTTPS'],
['114.230.106.95','48843','HTTPS'],
['114.230.41.33','3128','HTTP'],
['114.231.243.159','35387','HTTPS'],
['115.154.191.26','80','HTTP'],
['115.203.163.30','30286','HTTPS'],
['115.209.8.127','41338','HTTPS'],
['115.214.79.98','8118','HTTPS'],
['115.226.147.132','38006','HTTPS'],
['115.46.65.124','8123','HTTPS'],
['115.46.71.53','8123','HTTP'],
['115.46.71.75','8123','HTTPS'],
['115.46.75.91','8123','HTTP'],
['115.46.98.31','8123','HTTPS'],
['116.22.54.82','8118','HTTP'],
['116.3.205.22','8888','HTTP'],
['117.28.163.66','25909','HTTPS'],
['118.254.151.22','3128','HTTP'],
['119.164.19.25','8118','HTTP'],
['120.32.5.46','8118','HTTPS'],
['120.42.126.81','28333','HTTP'],
['121.228.98.51','8118','HTTP'],
['121.31.103.79','8123','HTTP'],
['121.31.146.158','8123','HTTP'],
['121.31.155.140','8123','HTTP'],
['121.31.155.211','8123','HTTP'],
['121.31.176.37','8123','HTTPS'],
['122.235.208.158','8118','HTTPS'],
['122.241.75.7','808','HTTP'],
['123.163.179.67','30090','HTTP'],
['124.228.239.185','3128','HTTP'],
['124.228.239.77','3128','HTTP'],
['125.105.107.133','3128','HTTPS'],
['125.112.174.44','29495','HTTPS'],
['125.41.207.103','8118','HTTP'],
['139.208.188.72','8118','HTTPS'],
['171.38.24.107','8123','HTTP'],
['171.39.115.64','8123','HTTP'],
['171.39.30.18','8123','HTTP'],
['171.39.40.88','8123','HTTP'],
['175.11.212.229','808','HTTPS'],
['180.113.46.229','8118','HTTP'],
['180.115.14.17','43267','HTTPS'],
['180.119.65.244','3128','HTTP'],
['180.122.150.56','20017','HTTPS'],
['180.155.134.186','21014','HTTPS'],
['180.175.133.135','8118','HTTP'],
['182.112.128.35','8118','HTTP'],
['183.145.48.186','8118','HTTP'],
['183.51.122.179','8118','HTTP'],
['221.10.159.234','1337','HTTP'],
['221.198.105.137','8118','HTTPS'],
['221.229.18.62','3128','HTTPS'],
['222.132.124.122','8118','HTTP'],
['222.76.144.206','39841','HTTP'],
['222.85.50.209','808','HTTP'],
['222.94.196.128','3128','HTTPS'],
['27.197.102.105','8118','HTTPS'],
['27.40.132.66','61234','HTTPS'],
['27.40.139.26','61234','HTTPS'],
['27.40.146.205','61234','HTTP'],
['27.40.157.24','61234','HTTP'],
['27.40.159.25','61234','HTTPS'],
['36.27.142.86','25217','HTTP'],
['36.27.142.86','25217','HTTPS'],
['39.75.172.201','8118','HTTPS'],
['49.71.81.160','3128','HTTPS'],
['49.71.81.214','3128','HTTPS'],
['49.71.81.29','3128','HTTP'],
['49.77.211.10','48606','HTTP'],
['49.83.31.220','808','HTTPS'],
['59.58.241.136','20934','HTTPS'],
['59.58.242.103','22280','HTTPS'],
['60.184.172.145','3128','HTTPS']]



IPList = []
for pos in IPoor:
	IPList.append([pos[2],("http://"+pos[0]+":"+pos[1])])	

conn=pymysql.connect(host="localhost",user="pytest",password="password",db="JDdb",port=3306,charset='utf8')
InsterSql="INSERT INTO IPOOR (HTTP,IPURL) VALUES (%s,%s)"
cur=conn.cursor() 
count=0
try:  
    for IP in IPList:
        cur.execute(InsterSql,IP)
        count=count+1
    conn.commit()
except Exception as e:  
    conn.rollback()
    raise e     
finally:  
    cur.close()
    conn.close()
print("Inster %d records into table"%count)