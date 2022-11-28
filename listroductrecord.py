#!C:\Users\Administrator\AppData\Local\Programs\Python\Python310\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
#連線DB
from dbConfig import conn, cur
import catalogue as cat
#先印出http 表頭
print("Content-Type: text/html; charset=utf-8\n")
#連續3個"""表多行字串
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>商品目錄</title>
</head>

<body>

 
""")
proList=cat.Listact()
for (pid,product,nums,price,act) in proList:
    if act==1:
        act='競標中'
    else:
        act='結標'
    print(f"""<p>編號{pid}: 商品:{product} 數量:{nums} 價格:{price} 狀態:{act} </p>""")
print("<hr></body></html>")