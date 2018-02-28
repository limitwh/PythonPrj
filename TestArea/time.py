__author__ = 'limitwh'
#coding=utf-8
import datetime
import pymysql
import time
conn=pymysql.connect(host="localhost",user="pytest",password="password",db="JDdb",port=3306,charset='utf8')
InsterSql="INSERT INTO HISTORY (HISITEMID,HISPRICE,GETTIMEVERSION) VALUES (%s,%s,%s)"
#updatetime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
#print("SET UpdTimeVersion = '"+str(updatetime)+"' WHERE CURITEMID=")
#Sreachsql="SELECT * FROM HISTORY"
#results = ((1, '5181396', 999.0, datetime.datetime(2018, 2, 25, 0, 51, 59)), (2, '5835285', 899.0, datetime.datetime(2018, 2, 25, 0, 54, 56)))
cur = conn.cursor()
try:
	updatetime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	print(str(updatetime))
	cur.execute(InsterSql,('666666',666.66,updatetime))
	conn.commit()
except Exception as e:  
	conn.rollback()
	raise e     
finally:  
	cur.close()
	conn.close()

#print(updatetime)