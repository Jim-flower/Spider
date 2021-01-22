import requests as r
from lxml import etree
import csv
r.adapters.DEFAULT_RETRIES = 5 # 增加重连次数
s = r.session()
s.proxies={"https": "http://121.233.227.138:9999", "http": "http://120.83.96.67:9999", }
s.keep_alive = False
url='https://www.kcsjgcsw.com/personal_show.php?showid=176'
headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
           "cookie":"LiveWSLZT73369086=173379c7ce5a4c5dbc36415a61f0b9f8; LiveWSLZT73369086sessionid=173379c7ce5a4c5dbc36415a61f0b9f8; NLZT73369086fistvisitetime=1611205804014; NLZT73369086visitecounts=1; NLZT73369086IP=%7C103.98.241.2%7C; UM_distinctid=1772359806ff4-0673a8a790c3d6-31346d-144000-177235980707ea; CNZZDATA1274190688=1027772437-1611205803-%7C1611205803; _qddaz=QD.uesm1o.zhjdou.kk6ec3uy; _qdda=3-1.1; tencentSig=2104454144; LeeUserType=2; LeeUserType__ckMd5=f12fcd05003c2a07; PHPSESSID=fcdlv4p30cfmfomd8i1h483615; IESESSION=alive; _qddab=3-82r69m.kk6fbvh5; _qddamta_4000088650=3-0; NLZT73369086lastshowinvite=1611209968917; _qddac=3-2-1.1.82r69m.kk6fbvh5; NLZT73369086lastvisitetime=1611210499311; NLZT73369086visitepages=45; NLZT73369086lastinvite=1611210502447; NLZT73369086LR_check_data=4%7C1611210502481%7C%7C%7C"
           }

if __name__ == '__main__':
    try:
        res = r.get(url,headers=headers,proxies=s.proxies)
        print(res.text)
        html = etree.HTML(res.text)
        # print(html.text)

        for x in html.xpath('//div[@class="conBox showinfo mb10"]'):  # 选定所有tr标签 其中第一项没有用
            f = open('data.csv', 'a+', encoding='utf-8',newline='')
            csv_writer = csv.writer(f)
            # print(x.xpath('./table[1]/tr[1]/td[2]/text()'))#这个是姓名
            # print(x.xpath('./table[2]/tr[2]/td[1]/text()'))#职业资格
            # print(x.xpath('./table[3]/tr[1]/td[2]/text()'))
            if len(x.xpath('./table[1]/tr[1]/td[2]/text()')):
                a=x.xpath('./table[1]/tr[1]/td[2]/text()')[0]
            if len(x.xpath('./table[2]/tr[2]/td[1]/text()')):
                b=x.xpath('./table[2]/tr[2]/td[1]/text()')[0]
            if len(x.xpath('./table[3]/tr[1]/td[2]/text()')):
                c=x.xpath('./table[3]/tr[1]/td[2]/text()')[0]
            csv_writer.writerow([a, b, c])






        #     print(x)



    except Exception as e:
        print(e)

