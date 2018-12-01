import requests as req
import zipfile, io
from bs4 import BeautifulSoup as bs
a = input()
r =req.get(r"https://www.imdb.com/find?ref_=nv_sr_fn&q={}&s=all".format(a)).text
soup = bs(r,"lxml")
link = soup.find("td",class_="result_text").a['href'].split('/')[2]
all = req.get(r"https://www.yifysubtitles.com/movie-imdb/{}".format(link)).text
s = bs(all,"lxml")
for best in s.find_all("tr",class_="high-rating"):
    if(best.find(class_="sub-lang").text=="English"):
        final = best.a["href"][11:]
zipp =  req.get(r"https://www.yifysubtitles.com/subtitle/{}.zip".format(final),stream=True)
z = zipfile.ZipFile(io.BytesIO(zipp.content))
z.extractall("F:\subtitles")


