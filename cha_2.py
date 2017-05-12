#-*- coding:utf-8 -*- - 
def str_c(x):
    m=0
    x=raw.split(" ")
    for per_str in x:
        per_str=list(map(ord,per_str))
        fo=" "
        for per_al in per_str:
            if per_al>=97 and per_al<=122:
                if per_al+2>122:
                    per_al=per_al-121+97
                else:
                    per_al+=2
            per_al=chr(per_al)
            fo=fo+per_al
        x[m]=fo
        m+=1
    fo=""
    for i in x:
        fo=fo+i
    print(fo)

raw="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
str_c(raw)
#join使用不了
#for不能改变原数据

#使用maketrans()函数
raw="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
def chan(x):
    fo=''
    for i in x:
        i=chr(i)
        fo=fo+i
    return fo
input=list(range(97,123))
output=list(range(99,123))
output.extend([97,98])
input=chan(input)
output=chan(output)
trantab=str.maketrans(input,output)
print (raw.translate(trantab))
