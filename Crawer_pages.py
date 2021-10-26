import bs4
import urllib.request as req  # 建立連線


def get_title(url):
    request = req.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
        "cookie": "over18=1"
    })

    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    root = bs4.BeautifulSoup(data, "html.parser")

    all_titles = root.find_all("div", class_="title")

    for title in all_titles:
        if title.a != None:
            print(title.a.string)
    next_url = root.find("a", string='‹ 上頁')  # 用文字去抓該屬性
    return "https://www.ptt.cc" + next_url['href']


url = "https://www.ptt.cc/bbs/Gossiping/index.html"

for i in range(3):  # 抓個3頁試試看
    url = get_title(url)
