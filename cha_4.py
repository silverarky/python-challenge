#-*- coding:utf-8 -*- - 
import requests
try:
    html=requests.get("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345")
    res=html.text
    #根据提示，400次就够了
    for i in range(400):
        print(res)
        ch_int=res.split()[-1]
        html=requests.get("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=s%" %ch_int)
        res=html.text
    print("loop is complete.")
except:
    print("Cannot open next website,or there are some problems in URL.")

#运行中会出现将前一个数除2的提示，如果无视提示也可在loop接近400次时得到结果
#当nothing=peak.html时网页依然能loop下去

#--------------------
#使用urllib.request模块
import urllib.request
import re
pattern=re.compile(r'(\d+)$')
nextnothing="12345"
i=0
while True:
    try:
        res=urlib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s" % nextnothing)
        result=res.read()
        res.close()
        print(result)
        oldnextnothing=nextnothing
        nextnothing=re.search(pattern,result).re.group()
        i+=1
    except:
        nextnothing=oldnextnothing
    
#通过设置pattern并结合search()找数字
#除2后运行中会出现"There maybe misleading numbers in the text. One example is 82683. Look only for the next nothing and the next nothing is 63579"的误导
#此方法可能会因此受误导


