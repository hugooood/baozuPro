#-*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from urlparse import urljoin
import requests
import csv

#原版
#url = "http://bj.58.com/pinpaigongyu/pn/{page}/?minprice=2000_4000"

#通用版
#url = "http://{local}.58.com/zufang/{value}/pn{page}/?"

#东营58租房版
url = "http://dy.58.com/chuzu/b1/pn{page}/?"

#已完成的页数序号，初时为0
page = 0

#新建csv文件
csv_file = open("rent_dy.csv","wb") 
csv_writer = csv.writer(csv_file, delimiter=',')

while True:
    page += 1
    print("fetch: ", url.format(page=page))
    response = requests.get(url.format(page=page))
    html = BeautifulSoup(response.text,'html5lib')
   
    #获取class=listUl的元素下的所有li元素
    house_list = html.select(".listUl > li")

    #print(house_list)
    # with open('house_list.txt','wb') as f:
    #     f.write(house_list)
    
    print('-----------node1---------------')    
    # 循环在读不到新的房源时结束
    if not house_list:
        break

    print('page:',page)
    print('house_list:',len(house_list))
    print('-----------')
    try:
        for house in house_list:
            house_title = house.select("h2 > a")[0].string.encode("utf-8")

            house_url = urljoin(url, house.select("a")[0]["href"])
            #print('house_url:',house_url)
            house_info_list = house_title.split()
            #print(house_info_list)
            
            #关键字匹配地址
            if "区" in house_info_list[2] or\
               "楼" in house_info_list[2] or\
               "村" in house_info_list[2] or\
               "房" in house_info_list[2] or\
               "街" in house_info_list[2] or\
               "城" in house_info_list[2] or\
               "花园" in house_info_list[2] or\
               "路" in house_info_list[2]:
                house_location = house_info_list[2]
            else:
                house_location = ' '

            house_money = house.select(".money")[0].select("b")[0].string.encode("utf8")
            csv_writer.writerow([house_title, house_location, house_money, house_url])
    except:
        continue
csv_file.close()