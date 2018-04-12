import requests
import json
class Request_method:
    #get请求
    def get_method(self,url,data,header=None):
        if header != None:
            res = requests.get(url=url,data=data,headers=header)
        else:
            res = requests.get(url=url,data=data)
        return res
    #post请求
    def post_method(self,url,data,header=None):
        if header != None:
            res = requests.post(url=url,data=data,headers=header)
        else:
            res = requests.post(url=url,data=data)
        return res.json()
    #判断请求方式后执行请求
    def run_requests(self,method,url,data=None,header=None):
        res = None
        if method == "get":
            res = self.get_method(url,data,header)
        else:
            res = self.post_method(url,data,header)
        return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)

if __name__ == "__main__":

    a = Request_method()
    res = a.run_requests("post","https://www.imooc.com/api3/userinfo")
    print(res)