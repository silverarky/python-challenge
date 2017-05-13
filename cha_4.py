#-*- coding:utf-8 -*- - 
#获取源码并保存
import requests
html=requests.get("http://www.pythonchallenge.com/pc/def/equality.html")
res=html.text.partition("<!--")[2]
with open("cha_4.txt","w") as data0:
    print(res,file=data0)
data0=open("cha_4.txt","r")
data1=open("cha_4a.txt","w")
#去掉空行并存为新文件
for i in data0:
    if i.split():
        data1.writelines(i)
data0.close()
data1.close()

#计算每行字符数,并整理成列表
with open("cha_4a.txt","r") as data1:
    res_list=data1.readlines()
    #去掉最后一行的"--!>"
    res_list.pop(-1)
with open("cha_4a.txt","r") as data1:
    num_alpha=len(data1.readline())
    
#计算字符"xXXXxXXXx"
sp=""
for i in res_list:
    for j in range(num_alpha-8):
        if i[j].islower():
            list_up=i[j+1]+i[j+2]+i[j+3]+i[j+5]+i[j+6]+i[j+7]
            list_lo=i[j+4]+i[j+8]
            if list_up.isupper()==True and list_lo.islower()==True:
                sp+=i[j+4]
print(sp)
#，打开文件后，使用其中一种read()类型函数【readline、readlines、read】时，不能使用另一种read()类型函数。重开文件后可重新使用。

#--------------------
#使用re模块中的findall函数
import re
import requests
html=requests.get("http://www.pythonchallenge.com/pc/def/equality.html")
res=html.text.partition("<!--")[2]
pattern="[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]"
sp=""
for i in re.findall(pattern,res):
    sp+=i[4]
print(sp)