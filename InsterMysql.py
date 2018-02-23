__author__ = 'limitwh'
#coding=utf-8
import pymysql
ItemList=[['19994179320', 'https://item.jd.com/19994179320.html', '华为（HUAWEI）Mate 10 Pro', '5399.00'], 
          ['21847456363', 'https://item.jd.com/21847456363.html', '华为（HUAWEI）荣耀V9 play', '1199.00'], 
          ['18377347431', 'https://item.jd.com/18377347431.html', '华为（HUAWEI） 荣耀 畅玩7X 全网通4G智能手机 铂光金 （4G+128G） 尊享版', '1999.00']]
db=pymysql.connect(host="localhost",user="pytest",password="password",db="JDdb",port=3306,charset='utf8')
InsterSql="""INSERT INTO CURRENT (CurItemId,ItemName,URL,CurPrice) VALUES(%s,%s,%s,%s)"""
cur = db.cursor() 
print(InsterSql)
try:  
    sts=cur.execute(InsterSql) 
    if sts==1:
        print("Done")
    else:
        print("Failed")
    db.commit()
except Exception as e:  
    db.rollback()
    raise e     
finally:  
    cur.close()
    db.close()