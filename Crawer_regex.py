from urllib.request import urlopen
import re

html = urlopen("https://mofanpy.com/static/scraping/basic-structure.html").read().decode('utf-8')

res = re.findall(r"<title>(.+?)</title>", html)  # find title
print("\nPage title is: ", res[0])

res = re.findall(r"<p>(.*?)</p>", html, flags=re.DOTALL)    # re.DOTALL if multi line
print("\nPage paragraph is: ", res[0])

res = re.findall(r'href="(.*?)"', html)  # find all link
print("\nAll links: ", res)