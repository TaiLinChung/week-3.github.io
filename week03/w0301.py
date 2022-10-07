# 串接串接。擷取公開資料
import urllib.request as request        #1.網路連線模組
import json                             #2.為了解讀json格式所以載入json模組
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:  #3.將網址中的資料整塊讀取下來
    data=json.load(response)    #4.利用json模組 處理 json 資料格式
# print(int(data["result"]["results"][0]["xpostDate"][:4])>2015)


##原作
# scopeList=data["result"]["results"]
# # print(scopeList)
# for eachScope in scopeList:
#     # print(eachScope)
#     if int(eachScope["xpostDate"][:4])>=2015:
#         allLink=eachScope["file"]
#         jpgPos=allLink.lower().find(".jpg")
#         # print(allLink[:jpgPos+4])
#         jpgLink=allLink[:jpgPos+4]
#         print(eachScope["stitle"]+","+eachScope["address"][5:8]+","+eachScope["longitude"]+","+eachScope["latitude"]+","+jpgLink)



##寫入
scopeList=data["result"]["results"]
with open("data.csv","w",encoding="utf-8-sig") as file:
    for eachScope in scopeList:
    # print(eachScope)
        if int(eachScope["xpostDate"][:4])>=2015:
            allLink=eachScope["file"]
            jpgPos=allLink.lower().find(".jpg")
            # print(allLink[:jpgPos+4])
            jpgLink=allLink[:jpgPos+4]
            # print(eachScope["stitle"]+","+eachScope["address"][5:8]+","+eachScope["longitude"]+","+eachScope["latitude"]+","+jpgLink)
            file.write(eachScope["stitle"]+","+eachScope["address"][5:8]+","+eachScope["longitude"]+","+eachScope["latitude"]+","+jpgLink+"\n")

    # for eachCompany in clist:
    #     file.write(eachCompany["公司名稱"]+"\n")