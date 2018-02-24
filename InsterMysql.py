__author__ = 'limitwh'
#coding=utf-8
import pymysql
ItemList=[['21690477583', 'https://item.jd.com/21690477583.html', '小米红米5Plus', '1299.00'], ['17701606448', 'https://item.jd.com/17701606448.html', '小米（MI）红米5A', '699.00'], ['4230903', 'https://item.jd.com/4230903.html', '小米小米Note3', '1999.00'], ['5911245', 'https://item.jd.com/5911245.html', '360N6 Lite', '999.00'], ['20347103098', 'https://item.jd.com/20347103098.html', '小米（MI）红米5 Plus', '1099.00'], ['17874263601', 'https://item.jd.com/17874263601.html', '华为（HUAWEI）荣耀7X', '1999.00'], ['12675634572', 'https://item.jd.com/12675634572.html', '华为（HUAWEI）荣耀畅玩6A', '629.00'], ['6008133', 'https://item.jd.com/6008133.html', '华为荣耀9青春版', '1199.00'], ['13164693176', 'https://item.jd.com/13164693176.html', '华为（HUAWEI） 华为P10 Plus 手机 曜石黑 全网通(6G+128G)', '3988.00'], ['14142420671', 'https://item.jd.com/14142420671.html', '华为（HUAWEI）荣耀9', '2699.00'], ['19094839248', 'https://item.jd.com/19094839248.html', '小米（MI）小米5X', '1499.00'], ['17349365291', 'https://item.jd.com/17349365291.html', '小米（MI）红米5 Plus', '1359.00'], ['20904886128', 'https://item.jd.com/20904886128.html', '华为（HUAWEI）荣耀V10', '3249.00'], ['13307299138', 'https://item.jd.com/13307299138.html', '小米（MI） 小米 红米note5A 手机 香槟金 全网通(3G+32G)支持指纹识别 标配', '899.00'], ['11266782788', 'https://item.jd.com/11266782788.html', '华为（HUAWEI）畅享7 Plus', '1699.00'], ['16514616213', 'https://item.jd.com/16514616213.html', '小米（MI）小米MIX2', '3499.00'], ['16431597101', 'https://item.jd.com/16431597101.html', '小米（MI）小米5X', '1999.00'], ['19265789676', 'https://item.jd.com/19265789676.html', '华为（HUAWEI）V10', '3099.00'], ['12652458939', 'https://item.jd.com/12652458939.html', '小米（MI）小米6', '3499.00'], ['18166164133', 'https://item.jd.com/18166164133.html', '华为（HUAWEI）mate10', '4499.00'], ['11544050480', 'https://item.jd.com/11544050480.html', '华为（HUAWEI）P10', '3488.00'], ['11565700466', 'https://item.jd.com/11565700466.html', '华为（HUAWEI） nova 手机 玫瑰金 移动全网(4G+64G)', '1699.00'], ['22858076134', 'https://item.jd.com/22858076134.html', '华为（HUAWEI）荣耀9青春版', '1226.00'], ['17347256002', 'https://item.jd.com/17347256002.html', '小米（MI）小米Max2', '1599.00'], ['20906779013', 'https://item.jd.com/20906779013.html', '华为（HUAWEI）荣耀V10', '3999.00'], ['20903934106', 'https://item.jd.com/20903934106.html', '华为（HUAWEI） 荣耀v10 手机 全面屏 幻夜黑 全网通(6G+64G)', '3099.00'], ['13486022186', 'https://item.jd.com/13486022186.html', '华为（HUAWEI） 荣耀 8青春版  全网通4G手机 幻海蓝 （4GB+32GB）高配版', '1399.00'], ['12740055091', 'https://item.jd.com/12740055091.html', '华为（HUAWEI） 华为nova2 plus 手机 玫瑰金 全网通移动版(4G+128G)标配', '3399.00'], ['4734101', 'https://item.jd.com/4734101.html', '魅族魅族PRO 7', '1999.00'], ['5996385', 'https://item.jd.com/5996385.html', 'vivoY75', '1498.00'], ['18167356217', 'https://item.jd.com/18167356217.html', '华为（HUAWEI） Mate10 手机 亮黑色 全网通(6G+128G)', '4999.00'], ['18377347431', 'https://item.jd.com/18377347431.html', '华为（HUAWEI） 荣耀 畅玩7X 全网通4G智能手机 铂光金 （4G+128G） 尊享版', '1999.00'], ['15027171956', 'https://item.jd.com/15027171956.html', '小米（MI） 小米note3 手机 亮黑色 全网通（6G RAM+64G ROM）标配', '2299.00'], ['5936828', 'https://item.jd.com/5936828.html', '华为荣耀V10', '2999.00'], ['4229972', 'https://item.jd.com/4229972.html', '努比亚Z11', '1799.00'], ['5963074', 'https://item.jd.com/5963074.html', '360N6', '1399.00'], ['12671748777', 'https://item.jd.com/12671748777.html', '小米（MI） 红米Note4X 全网通4G 移动联通电信全网通4G智能手机 磨砂黑 4G+64', '1399.00'], ['21678745124', 'https://item.jd.com/21678745124.html', '华为（HUAWEI） 华为nova2S 全面屏手机 曜石黑 全网通(6G+64G)', '2999.00'], ['18180585426', 'https://item.jd.com/18180585426.html', '华为（HUAWEI）Mate 10 Pro', '5999.00'], ['5484048', 'https://item.jd.com/5484048.html', '魅族魅蓝6', '699.00'], ['14062633583', 'https://item.jd.com/14062633583.html', '小米（MI）小米5X', '1499.00'], ['22862675837', 'https://item.jd.com/22862675837.html', '华为（HUAWEI） 荣耀9青春版 手机 魅海蓝 全网通（4GB+32GB）高配版', '1899.00'], ['22889126293', 'https://item.jd.com/22889126293.html', '华为（HUAWEI）荣耀9青春版', '1599.00'], ['11704358260', 'https://item.jd.com/11704358260.html', '华为（HUAWEI）Nova青春版', '1319.00'], ['14507356150', 'https://item.jd.com/14507356150.html', '华为（HUAWEI）畅享6', '899.00'], ['10781492357', 'https://item.jd.com/10781492357.html', '华为（HUAWEI）nova', '1429.00'], ['18717872466', 'https://item.jd.com/18717872466.html', '小米（MI） 小米(MI) 小米5X 手机 红色特别版 全网通（4G RAM+64G ROM）标配版', '1499.00'], ['17760675843', 'https://item.jd.com/17760675843.html', '华为（HUAWEI） 荣耀V9 全网通 移动联通电信4G双卡双待 智能手机 幻夜黑 全网通(6G+128G)', '3499.00'], ['21676582420', 'https://item.jd.com/21676582420.html', '小米（MI）小米 红米5 Plus', '1999.00'], ['5835261', 'https://item.jd.com/5835261.html', '小米红米5 Plus', '999.00'], ['20067198287', 'https://item.jd.com/20067198287.html', '华为（HUAWEI）荣耀V10', '3699.00'], ['22870372857', 'https://item.jd.com/22870372857.html', '华为（HUAWEI） 荣耀9青春版 全面屏手机 魅海蓝 全网通(4G+64G)', '1799.00'], ['16006919584', 'https://item.jd.com/16006919584.html', '华为（HUAWEI）荣耀畅玩6', '699.00'], ['16288642023', 'https://item.jd.com/16288642023.html', '华为（HUAWEI） 荣耀 V9 play  手机 极光蓝 全网通4G（4GB+32GB）', '1399.00'], ['10833486405', 'https://item.jd.com/10833486405.html', '华为（HUAWEI） 荣耀6X 畅玩6X 手机 冰河银 全网通(3GB+32GB)公开版', '1399.00'], ['19994179320', 'https://item.jd.com/19994179320.html', '华为（HUAWEI）Mate 10 Pro', '5399.00'], ['21847456363', 'https://item.jd.com/21847456363.html', '华为（HUAWEI）荣耀V9 play', '1199.00'], ['19079219127', 'https://item.jd.com/19079219127.html', '华为（HUAWEI） 荣耀V9 Play 手机 极光蓝 全网通 标配(3G+32G )', '888.00'], ['21962516326', 'https://item.jd.com/21962516326.html', '华为（HUAWEI）荣耀9青春版', '1599.00'], ['11259202658', 'https://item.jd.com/11259202658.html', '小米（MI）红米4A', '599.00'], ['17876272248', 'https://item.jd.com/17876272248.html', '华为（HUAWEI） 荣耀7X 畅玩7X 全面屏 手机 幻夜黑 全网通(4G+64G)', '2099.00'], ['10971696962', 'https://item.jd.com/10971696962.html', '魅族（MEIZU） 魅族5 魅蓝5 手机 冰河白 全网通4G(2G RAM+16G ROM)标配', '599.00'], ['15312744320', 'https://item.jd.com/15312744320.html', '小米（MI）小米MIX2', '4599.00']]
db=pymysql.connect(host="localhost",user="pytest",password="password",db="JDdb",port=3306,charset='utf8')
InsterSql="INSERT INTO CURRENT (CurItemId,URL,ItemName,CurPrice) VALUES (%s,%s,%s,%s)"
cur = db.cursor() 
count=0
try:  
    for Item in ItemList:
        cur.execute(InsterSql,Item)
        count=count+1
    db.commit()
except Exception as e:  
    db.rollback()
    raise e     
finally:  
    cur.close()
    db.close()
print("Inster %d records into table"%count)