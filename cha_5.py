#-*- coding:utf-8 -*- - 
#获取源码并保存
import urllib.request as urllib
import pickle
import pprint
html=urllib.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
res=pickle.Unpickler(html).load()
pprint.pprint(res)

for i in res:
    sp=""
    for j in i:
        for k in range(j[1]):
            sp+=j[0]
    print(sp)

#--------------------
#循环部分优化
for i in res:
    print("".join([t[0]*t[1] for t in i]))

#join需要定义sep,不然会有NameError
        