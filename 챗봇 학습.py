import requests

readData=[]
strings=open("strings.txt","r",encoding="UTF-8").read().split("\n")
readData=open("read.txt","r",encoding="UTF-8").read().split("\n")

#data.write()
while 1:
    try:
        articleDatas=requests.post("https://playentry.org/graphql",data=("{\"query\":\"query SELECT_ENTRYSTORY($pageParam:PageParam$query:String$user:String$category:String$term:String$prefix:String$progress:String$discussType:String$searchType:String$searchAfter:JSON){discussList(pageParam:$pageParam query:$query user:$user category:$category term:$term prefix:$prefix progress:$progress discussType:$discussType searchType:$searchType searchAfter:$searchAfter){list{\\tid content}}}\",\"variables\":{\"category\":\"free\",\"searchType\":\"scroll\",\"term\":\"all\",\"discussType\":\"entrystory\",\"pageParam\":{\"display\":25,\"sort\":\"created\"}}}").encode("utf-8"),headers={"Content-Type":"application/json; charset=utf-8"}).json()["data"]["discussList"]["list"]
        print("처음부터 다시 검색합니다")
        for articleData in articleDatas:
            print("새로운 글을 검색합니다")
            try:
                commentDatas=requests.post("https://playentry.org/graphql",data=("{\"query\":\"query SELECT_COMMENTS($pageParam:PageParam$target:String$searchAfter:JSON$likesLength:Int$groupId:ID){commentList(pageParam:$pageParam target:$target searchAfter:$searchAfter likesLength:$likesLength groupId:$groupId){list{id content user{nickname}}}}\",\"variables\":{\"target\":\""+articleData["id"]+"\",\"pageParam\":{\"display\":10}}}").encode("utf-8"),headers={"Content-Type":"application/json; charset=utf-8"}).json()["data"]["commentList"]["list"]
                for commentData in commentDatas:
                    for a in list(map(str,articleData["content"].split())):
                        if a not in strings:
                            f=open("strings.txt","a",encoding="UTF-8")
                            #print(a)
                            f.write(a+"\n")
                            f.close()
                    if commentData["id"] not in readData:
                        stringData=[]
                        #print(stringData)
                        strings=open("strings.txt","r",encoding="UTF-8").read().split("\n")
                        for string in strings:
                            #print(string)
                            #print(string in articleData["content"])
                            #print(1)
                            if string in articleData["content"]:#pass
                                #print(1)
                                stringData.append({"text":string,"pos":articleData["content"].find(string)})
                                #print(stringData)
                        for i in range(len(stringData)):
                            for j in range(0,len(stringData)-i-1):
                                if stringData[j]["pos"]>stringData[j+1]["pos"]:
                                    stringData[j],stringData[j+1]=stringData[j+1],stringData[j]
                        print(stringData)
                        data=open("data.txt","a")
                        stringData2=[]
                        for a in stringData:
                            stringData2.append(a["text"])
                            #print(stringData)
                        stringData2.insert(0,commentData["content"].replace("\n","\\n")+"")
                        data.write(("".join(stringData2))+"\n")
                        data.close()
                        read=open("read.txt","a")
                        read.write(commentData["id"]+"\n")
                        readData.append(commentData["id"])
                        read.close()
                        print("".join(stringData))
            except:pass
    except:pass
