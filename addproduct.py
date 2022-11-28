#!C:\Users\Administrator\AppData\Local\Programs\Python\Python310\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import catalogue as ca
#連線DB
from dbConfig import conn, cur
#先印出http 表頭
print("Content-Type: text/html; charset=utf-8\n")
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>商品新增</title>
</head>
<body>
""")

#查詢
form = cgi.FieldStorage()
deadline=form.getvalue('deadline')
name=form.getvalue('Pname')
price=int(form.getvalue('price'))
if ca.addProduct(name,deadline,price):
    print("已新增")
else:
    print("新增失敗")
print("<br><a href='manageproduct.py'>回商品列表</a>")
print("</body></html>")