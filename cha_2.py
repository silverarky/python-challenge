#-*- coding:utf-8 -*- - 
import requests
#获取源码
html=requests.get("http://www.pythonchallenge.com/pc/def/ocr.html")
res=html.text

#判断字符
sp=""
for i in res:
    if i.isalpha():
        sp+=i
#源代码的判断部分从"find rare characters in the mess below"开始
sp=sp.partition("below")[2]

print(sp)

#--------------------
#计算最少字符数
raw="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
list=[]
keys=[]
for i in raw:
    list.append(i)
    if not i in keys:
        keys.append(i)
for i in keys:
    print(i,list.count(i))
    
#count只能用于列表

#--------------------
#利用dict下的Counter子类
import collections as cl
coun=cl.Counter()
for x in raw:
    coun[x]+=1
    print(coun)
    
