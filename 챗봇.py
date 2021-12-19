import random,requests
cookies={}
def Erequests(asdf,data):
    global cookies
    r=requests.post("https://playentry.org/graphql",data=(data).encode("utf-8"),headers={"Content-Type":"application/json; charset=utf-8"},cookies=cookies)
    if asdf:
        cookies=r.cookies.get_dict()
    return r.json()
strings=open("strings.txt","r",encoding="UTF-8").read().split("\n")
readData=open("articleRead.txt","r",encoding="UTF-8").read().split("\n")
data=open("data.txt","r").read().split("\n")
for i in range(len(data)):
    data[i]=data[i].split("")
    #print(data[i][1].split(""))
    try:
        data[i][1]=data[i][1].split("")
    except:pass
#print(data)
account=open("계정.txt","r").read().split()
while 1:
    data=open("data.txt","r").read().split("\n")
    for i in range(len(data)):
        data[i]=data[i].split("")
        #print(data[i][1].split(""))
        try:
            data[i][1]=data[i][1].split("")
        except:pass
    try:
        articleDatas=requests.post("https://playentry.org/graphql",data=("{\"query\":\"query SELECT_ENTRYSTORY($pageParam:PageParam$query:String$user:String$category:String$term:String$prefix:String$progress:String$discussType:String$searchType:String$searchAfter:JSON){discussList(pageParam:$pageParam query:$query user:$user category:$category term:$term prefix:$prefix progress:$progress discussType:$discussType searchType:$searchType searchAfter:$searchAfter){list{\\tid content}}}\",\"variables\":{\"category\":\"free\",\"searchType\":\"scroll\",\"term\":\"all\",\"discussType\":\"entrystory\",\"pageParam\":{\"display\":25,\"sort\":\"created\"}}}").encode("utf-8"),headers={"Content-Type":"application/json; charset=utf-8"}).json()["data"]["discussList"]["list"][0]
        if articleDatas["id"] not in readData:
            read=articleDatas["content"]
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
                outString=output[random.randrange(0,len(output))]
                login=Erequests(True,"{\"query\":\"mutation($username:String!,$password:String!,$rememberme:Boolean,$captchaValue:String,$captchaKey:String,$captchaType:String){signinByUsername(username:$username,password:$password,rememberme:$rememberme,captchaValue:$captchaValue,captchaKey:$captchaKey,captchaType:$captchaType){id nickname role isEmailAuth}}\",\"variables\":{\"username\":\""+account[0]+"\",\"password\":\""+account[1]+"\"}}")
                asdf=Erequests(True,"{\"query\":\"mutation CREATE_COMMENT($content:String$image:String$sticker:String$target:String$targetSubject:String$targetType:String$groupId:ID){createComment(content:$content image:$image sticker:$sticker target:$target targetSubject:$targetSubject targetType:$targetType groupId:$groupId){warning}}\",\"variables\":{\"content\":\"[챗봇 테스트중] "+outString+"\",\"target\":\""+articleDatas["id"]+"\",\"targetSubject\":\"discuss\",\"targetType\":\"individual\"}}")
                print("로그인:",login)
                print("글적기:",asdf)
                read=open("articleRead.txt","a")
                read.write(articleDatas["id"]+"\n")
                readData.append(articleDatas["id"])
                read.close()
                print("댓글 추가:",outString)
            except:pass
    except:pass
