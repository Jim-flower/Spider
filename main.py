import requests as r
from lxml import etree
import csv
import time
import os
import warnings
from getip import *
from multiprocessing import Process
warnings.filterwarnings("ignore")
r.adapters.DEFAULT_RETRIES = 5 # 增加重连次数
s = r.session()

proxies={"https": "https://117.69.168.75:20701", "http": "http://117.69.168.75:20701", }
s.keep_alive = False
ipurl=url ="http://ip.ipjldl.com/index.php/api/entry?method=proxyServer.hdtiqu_api_url&packid=0&fa=0&groupid=0&fetch_key=&time=102&qty=1&port=1&format=txt&ss=1&css=&dt=0&pro=&city=&usertype=4"
url ="https://www.kcsjgcsw.com/personal.php?PageNo="
headers = {'Connection':'close',
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
           "cookie":"LiveWSLZT73369086=173379c7ce5a4c5dbc36415a61f0b9f8; LiveWSLZT73369086sessionid=173379c7ce5a4c5dbc36415a61f0b9f8; NLZT73369086fistvisitetime=1611205804014; NLZT73369086visitecounts=1; NLZT73369086IP=%7C103.98.241.2%7C; UM_distinctid=1772359806ff4-0673a8a790c3d6-31346d-144000-177235980707ea; CNZZDATA1274190688=1027772437-1611205803-%7C1611205803; _qddaz=QD.uesm1o.zhjdou.kk6ec3uy; _qdda=3-1.1; tencentSig=2104454144; LeeUserType=2; LeeUserType__ckMd5=f12fcd05003c2a07; PHPSESSID=fcdlv4p30cfmfomd8i1h483615; IESESSION=alive; _qddab=3-82r69m.kk6fbvh5; _qddamta_4000088650=3-0; NLZT73369086lastshowinvite=1611209968917; _qddac=3-2-1.1.82r69m.kk6fbvh5; NLZT73369086lastvisitetime=1611210499311; NLZT73369086visitepages=45; NLZT73369086lastinvite=1611210502447; NLZT73369086LR_check_data=4%7C1611210502481%7C%7C%7C"
           }

# url ="https://www.kcsjgcsw.com/personal.php?PageNo="
urls=[url+str(m) for m in range(183,269)]
domin="www.kcsjgcsw.com"
def generate_one(url):
    onelist=[]
    # print("HelloWorldAndSpider!!!")
    try:
        res = r.get(url, headers=headers,proxies=proxies,verify=False)
        # print(res.text)
        html = etree.HTML(res.text)
        for x in html.xpath('//tr'):  # 选定所有tr标签 其中第一项没有用
            # print(x.xpath('./@onclick')) #获取每一页的相对网址
            if len(x.xpath('./@onclick')):
                a = x.xpath('./@onclick')[0].split('(')  # 获取每一页的相对网址
                b = a[1].split(")")
                if b:
                    # print(domin + b[0].split("'")[1])
                    onelist.append(domin + b[0].split("'")[1])
        print("第二步")
        return onelist
    except Exception as e:
        # k = r.get(ipurl).text
        # try:
        #     res = r.get(url).text
        # except Exception:
        #     time.sleep(3)
        #     res = r.get(url).text

        # KK =input("请输入:")
        KK=Work()
        proxies["https"] = "http://" + KK
        proxies["http"] = "http://" + KK
        print(e)
        # print(proxies["https"])
        # time.sleep(10)
        return generate_one(url)

def generatetwo(url):
    try:
        res = r.get(url, headers=headers,proxies=proxies,verify=False )
        # print(res.text)
        html = etree.HTML(res.text)
        # print(html.text)

        for x in html.xpath('//div[@class="conBox showinfo mb10"]'):  # 选定所有tr标签 其中第一项没有用
            f = open('data.csv', 'a+', encoding='utf-8', newline='')
            csv_writer = csv.writer(f)
            # print(x.xpath('./table[1]/tr[1]/td[2]/text()'))#这个是姓名
            # print(x.xpath('./table[2]/tr[2]/td[1]/text()'))#职业资格
            # print(x.xpath('./table[3]/tr[1]/td[2]/text()'))
            if len(x.xpath('./table[1]/tr[1]/td[2]/text()')):
                a = x.xpath('./table[1]/tr[1]/td[2]/text()')[0]
            if len(x.xpath('./table[2]/tr[2]/td[1]/text()')):
                b = x.xpath('./table[2]/tr[2]/td[1]/text()')[0]
            if len(x.xpath('./table[3]/tr[1]/td[2]/text()')):
                c = x.xpath('./table[3]/tr[1]/td[2]/text()')[0]
            csv_writer.writerow([a, b, c])
            return 0
    except Exception as e:
        print(e)
        print("e2\n")
        # time.sleep(3)

        # k=r.get(ipurl).text
        # KK = input("请输入:")
        KK = Work()
        proxies["https"] = "http://" + KK
        proxies["http"] = "http://" + KK
        # time.sleep(10)
        return generatetwo(url)
def first(a,b):
    urls = [url + str(m) for m in range(a, b)]
    for urll in urls:
        # time.sleep(1)
        l = generate_one(urll)
        print("第一步")
        print("坐标："+str(urls.index(urll)))
        if len(l):
            for x in l:
                y = "https://" + x
                # print()
                generatetwo(y)
        else:
            print(l)
def main():
  print("主进程执行中>>> pid={0}".format(os.getpid()))
  ps=[]
  # 创建子进程实例

  p1=Process(target=first,name="worker1",args=(90,101))
  p2 = Process(target=first, name="worker2", args=(101, 112))
  p3 = Process(target=first, name="worker2", args=(112, 123))
  p4 = Process(target=first, name="worker2", args=(123, 134))

  # 开启进程
  p1.start()
  p2.start()
  p3.start()
  p4.start()
  # 阻塞进程
  p1.join()
  p2.join()
  p3.join()
  p4.join()
  print("主进程终止")
if __name__ == '__main__':
    main()





    # print(html.xpath('//tr/td[1]/text()'))
    # print(html.xpath('//tr/@onclick'))

