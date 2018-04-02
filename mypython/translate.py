import requests
import json
import time

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"}
while True:
    trans = input("请输入要翻译的文字（想退出翻译输入：q!）：")
    if trans == "q!":
        break
    data = {"i":trans,
                "from": "AUTO",
                "to": "AUTO",
                "smartresult": "dict",
                "client": "fanyideskweb",
                "salt": "1522647787167",
                "sign": "d77820d69e7cf6a1fc25a0888e0e4a6e",
                "doctype": "json",
                "version": "2.1",
                "keyfrom": "fanyi.web",
                "action": "FY_BY_CLICKBUTTION",
                "typoResult": "true"}
    
    res = requests.post(url,data=data,headers=header)
    s = json.loads(res.text)
    print(s["translateResult"][0][0]["tgt"])
    time.sleep(2)