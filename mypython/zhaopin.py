
from urllib import request
from bs4 import BeautifulSoup
import pymysql

db = {"host":'127.0.0.1',
      "port":3306,
      "user":'root',
      "passwd":��***��,
      "db":'t1',
      "charset" : "utf8"}
conn = pymysql.Connect(**db)
cursor = conn.cursor()
sql = "insert into lagou(positionname,time,company,salary,link) VALUES (%s, %s, %s, %s, %s)"
urls = ["https://www.lagou.com/zhaopin/ceshigongchengshi/1/?filterOption=1",
       "https://www.lagou.com/zhaopin/ceshigongchengshi/2/?filterOption=2",
       "https://www.lagou.com/zhaopin/ceshigongchengshi/3/?filterOption=3",
       "https://www.lagou.com/zhaopin/ceshigongchengshi/4/?filterOption=4",
       "https://www.lagou.com/zhaopin/ceshigongchengshi/5/?filterOption=5"]
f = open("lagou_data.txt", "w", encoding="utf-8")
header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"}
for url in urls:
    html = request.Request(url,headers=header)
    page = request.urlopen(html).read().decode("utf-8")
    soup = BeautifulSoup(page,"html.parser")
    all = soup.findAll("li",{"class":"con_list_item default_list"})
    for job_info in all:
        item = {}
        item["company"] = job_info.attrs["data-company"]
        item["positionname"] = job_info.attrs["data-positionname"]
        item["salary"] = job_info.attrs["data-salary"]
        item["link"] = job_info.find("a",{"class":"position_link"}).attrs["href"]
        item["time"]  = job_info.find("span",{"class":"format-time"}).get_text()

        try:
            cursor.execute(sql, (item['positionname'],
                                 item['time'],
                                 item['company'],
                                 item['salary'],
                                 item['link']))
            conn.commit()
        except pymysql.Error as e:
            # 若存在异常则抛出
            print(e.args)




