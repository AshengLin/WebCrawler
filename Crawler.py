import csv
import re

# 抓網頁原始碼(HTML)
import urllib.request as req  # 建立連線
url = "https://www.ptt.cc/bbs/iOS/index.html"

# 建立request object
# F12 > Network > index.html > headers > request headers (使用者瀏覽網頁通常發出的相關資訊) > user-agent
# 要讓網站認為你是普通使用者
request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
})

# with req.urlopen(url) as response:  # 原本放url，改request 附加資訊
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")  # 若不建立request object, 連線會被拒絕


# 抓出想要的部分
import bs4
root = bs4.BeautifulSoup(data, "html.parser")  # 用bs4協助整理html格式資訊
# print(root.title)  # 抓title的標籤和文字
# print(root.title.string)  # 該文字
# 找出你要的資料的標籤特色 ex: 標題前面都有 div
titles = root.find("div", class_="title")  # 找出class=title的div標籤  # root.find 會只找一個
# print(titles.a.string)  # ex:假如你抓出來有<a href=""> 包裹你的文字 用.a.string 去除
all_titles = root.find_all("div", class_="title")  # root.find_all 會找全部 , as a list
for title in all_titles:
    if title.a != None:  # 若標題有a標籤 則印出來
        with open('./PPT_IOS_titles.csv', 'a', newline='\n') as myfile:
            writer = csv.writer(myfile)
            writer.writerow([title.a.string])
            print(title.a.string)  # string
            print(title.a['href'])  # 屬性值


root.find_all('script', limit=2)  # 限制數量
result = root.find('a', href="/bbs/iOS/M.1635604231.A.980.html")  # 找到該位置
result.find_parent('div')  # 往回找父節點，找到div部分
root.select('div')  # 篩選標籤 label = div部分
root.select('.item')  # 篩選class = item部分

test = root.find('title')
test.find_previous_siblings("meta")  # 前節點
test.find_next_siblings("link", limit=1)  # 後節點
