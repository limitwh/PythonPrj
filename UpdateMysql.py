__author__ = 'limitwh'
#coding=utf-8
import pymysql
db=pymysql.connect(host="localhost",user="pytest",password="password",db="shopdb",port=3306,charset='utf8')
UpdateSql="""UPDATE goodstable set Gnum=5 WHERE Gname='卤鸡蛋'"""
cur = db.cursor()  
print(UpdateSql)
try:  
    sts=cur.execute(UpdateSql) 
    if sts==1:
        print("Done")
    else:
        print("Failed")
    db.commit()
except Exception as e:  
    db.rollback()
    raise e     
finally:  
    db.close()