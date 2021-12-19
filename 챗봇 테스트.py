import random
data=open("data.txt","r").read().split("\n")
strings=open("strings.txt","r",encoding="UTF-8").read().split("\n")
for i in range(len(data)):
    data[i]=data[i].split("")
    #print(data[i][1].split(""))
    try:
        data[i][1]=data[i][1].split("")
    except:pass
#print(data)
while 1:
    read=input(">>")
    stringData=[]
    for string in strings:
        if string in read:
            stringData.append({"text":string,"pos":read.find(string)})
    for i in range(len(stringData)):
        for j in range(0,len(stringData)-i-1):
            if stringData[j]["pos"]>stringData[j+1]["pos"]:
                stringData[j],stringData[j+1]=stringData[j+1],stringData[j]
    output=[]
    for d in data:
        try:
            a=0
            for s1 in stringData:
                for s2 in d[1]:
                    #print(s1["text"],s2)
                    #rint(s1["text"])
                    if s1["text"]==s2 and s1["text"]!="":
                        a+=1
            if len(d[1])-a<=3 and a>0:
                output.append(d[0])
                #print(d[0])
            #print(a)
        except:pass
    try:
        print(output[random.randrange(0,len(output))])
    except:pass
