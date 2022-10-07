#抓取PTT八卦版的網頁原始碼(HTML)
import urllib.request as req

def getData(url):
    

    #建立一個Request物件，附加Request Headers的資訊，******讓程式更像正常使用者******
    request=req.Request(url,headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    })#User-Agent告訴對方伺服器我們用的是哪個瀏覽器，哪個作業系統，好讓他們認為我們是一般使用者
    with req.urlopen(request) as response: #利用Request物件去打開網址
        data=response.read().decode("utf-8")
    # print(data)




    #解析原始碼，取得每篇文章的標題
    import bs4
    root=bs4.BeautifulSoup(data,"html.parser")  #(網頁html原始資料,"html.parser")
    # print(root.title)                         #root代表整份網頁.title title標籤的所有資訊
    # print(root.title.string)                  #.title.string title標籤的內文資訊
    # titles=root.find("div",class_="title")      #BeautifulSoup內件套件，尋找class="title"的div標籤
    # print(titles.a.string)                      #.a.string  a標籤的內文資訊




    ##網羅網頁內所有標題
    titles=root.find_all("div",class_="title")      #BeautifulSoup內件套件，尋找所有class="title"的div標籤
    # print(titles)                      #.a.string  a標籤的內文資訊


    for title in titles:
        if (title.a!=None):              #如果標題包含a標籤(沒有被刪除)
            # print(title.a.string)
            if "[好雷]" in title.a.string or "[ 好雷]" in title.a.string or "[好雷 ]" in title.a.string:
                goodList.append(title.a.string.replace(" ",""))
            elif "[普雷]" in title.a.string or "[ 普雷]" in title.a.string or "[普雷 ]" in title.a.string:
                commonList.append(title.a.string.replace(" ",""))
            elif "[負雷]" in title.a.string or "[ 負雷]" in title.a.string or "[負雷 ]" in title.a.string:
                badList.append(title.a.string.replace(" ",""))



    ###抓取上一頁連結
    nextLink=root.find("a",string="‹ 上頁") #根據內文，找到內文是"‹ 上頁"的a標籤
    # print(nextLink)       #此內容承接上方為完整a標籤
    # print(nextLink["href"]) #取出標籤內href屬性的內文
    return nextLink["href"]


##抓取一個頁面的標題
pageURL="https://www.ptt.cc/bbs/movie/index.html"
count=0
goodList=[]
commonList=[]
badList=[]
while count<10:
    pageURL="https://www.ptt.cc"+getData(pageURL)
    count+=1

# print(badList)
##寫入
with open("movie.txt","w",encoding="utf-8-sig") as file:
    for item in goodList:
        if "Re" not in item:
            file.write(item+"\n")
    for item in commonList:
        if "Re" not in item:
            file.write(item+"\n")
    for item in badList:
        if "Re" not in item:
            file.write(item+"\n")
