# encding:utf-8
import requests
url = "https://www.qijigps.com/api/v2.6/authentication"  
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
          "Content-type": "application/json; charset=UTF-8",
          "Cookie": "Hm_lvt_70fd7de5d5d3c9fe153258281c8e8c3e=1511185503,1511358181,1511361030,1511575694; Hm_lpvt_70fd7de5d5d3c9fe153258281c8e8c3e=1511576480",
          "Accept": "application/json, text/plain, */*",
          "Accept-Encoding": "gzip, deflate, br",
          "Accept-Language": "zh-CN,zh;q=0.8"
          }
body = {"username": "13631260632",
        "password": "96e79218965eb72c92a549dd5a330112",
        "remember_me": 0
        }

r = requests.post(url=url, json=body, headers=header, verify=False)
print r.content
