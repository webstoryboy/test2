import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd

titleList = []

res = req.get("https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query=%EC%86%8D%EB%B3%B4")
soup = bs(res.text, "lxml")
title = soup.select("a.news_tit")
for i in title :
    titleList.append(i.text)
    
dic = {"뉴스제목": titleList}
df = pd.DataFrame(dic)
df.to_csv("data.csv", encoding="utf-8", index=False)
