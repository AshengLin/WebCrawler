import bs4
import urllib.request as req  # 建立連線

# 抓網頁原始碼(HTML)
url = "https://www.ptt.cc/bbs/Gossiping/index.html"  # 八卦版有18歲彈出警告畫面
# F12> > Application > Storage > Cookies > https://www.ptt.cc > over18 = 1

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
    "cookie": "over18=1"
})  # cookie有時候就需要這樣增添憑證

with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

root = bs4.BeautifulSoup(data, "html.parser")
all_titles = root.find_all("div", class_="title")  # root.find_all 會找全部 , as a list
for title in all_titles:
    if title.a != None:  # 若標題有a標籤 則印出來
        print(title.a.string)
