import requests
from urllib.request import quote
from bs4 import BeautifulSoup
import json


def queryByKeyWord(keyword):
    url = 'http://trash.lhsr.cn/sites/feiguan/trashTypes_2/TrashQuery_h5.aspx?kw=' + quote(keyword)
    response = requests.get(url)

    soup=BeautifulSoup(response.text,"lxml")
    res=soup.select("div .info")
    if len(res) > 0:
        span = res[0].select("span")
        return span[0].get_text()
    return None

def getSuggest(keyword):
    url = 'http://trash.lhsr.cn/sites/feiguan/trashTypes/dyn/Handler/Handler.ashx'
    data = {"a": "Keywords_Get",
            "s_kw": quote(keyword),
           }

    response = requests.post(url=url, data=data, timeout=10)
    return response.text


suggestResult= ["小龙虾","龙虾","小龙虾壳"]
print(json.dumps(suggestResult,ensure_ascii=False))