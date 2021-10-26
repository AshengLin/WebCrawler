import urllib.request as req  # 建立連線
import bs4
import pandas as pd

"""
method I. 抓table還是用pandas比較容易
"""

url = "https://rate.bot.com.tw/xrt"
dfs = pd.read_html(url)
print(dfs[0])  # 表格部分都會存放於[0]   # 最簡單也最快

"""
method II. 依照格子去抓，比較麻煩
"""

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

root = bs4.BeautifulSoup(data, "html.parser")  # 用bs4協助整理html格式資訊
cash_name = root.find_all('div', {'class': "visible-phone print_hide"})
form = root.find_all('td', {'class': 'text-right display_none_print_show print_width',
                            'data-table': ["本行現金買入", "本行現金賣出", "本行即期買入", "本行即期賣出"]})  # 抓td 比較麻煩
for i in range(len(cash_name)):
    print(cash_name[i].text.strip())
    print("本行現金買入", form[i * 4].text)
    print("本行現金賣出", form[i * 4 + 1].text)
    print("本行即期買入", form[i * 4 + 2].text)
    print("本行即期賣出", form[i * 4 + 3].text)