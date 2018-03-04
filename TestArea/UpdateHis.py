__author__ = 'limitwh'
#coding=utf-8
import pymysql
conn=pymysql.connect(host="localhost",user="pytest",password="password",db="JDdb",port=3306,charset='utf8')
Sreachsql="SELECT CurItemId,CurPrice,UpdTimeVersion FROM CURRENT"
InsterSql="INSERT INTO HISTORY (HisItemId,HisPrice,GetTimeVersion) VALUES (%s,%s,%s)"
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
print("Inster %d records into table"%count)