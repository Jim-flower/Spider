import requests as r
from lxml import etree
# import time
url ="https://www.kcsjgcsw.com/personal.php?PageNo=1"
urls=[url+str(m) for m in range(1,20)]
headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
           "cookie":"LiveWSLZT73369086=173379c7ce5a4c5dbc36415a61f0b9f8; LiveWSLZT73369086sessionid=173379c7ce5a4c5dbc36415a61f0b9f8; NLZT73369086fistvisitetime=1611205804014; NLZT73369086visitecounts=1; NLZT73369086IP=%7C103.98.241.2%7C; UM_distinctid=1772359806ff4-0673a8a790c3d6-31346d-144000-177235980707ea; CNZZDATA1274190688=1027772437-1611205803-%7C1611205803; _qddaz=QD.uesm1o.zhjdou.kk6ec3uy; _qdda=3-1.1; tencentSig=2104454144; LeeUserType=2; LeeUserType__ckMd5=f12fcd05003c2a07; PHPSESSID=fcdlv4p30cfmfomd8i1h483615; IESESSION=alive; _qddab=3-82r69m.kk6fbvh5; _qddamta_4000088650=3-0; NLZT73369086lastshowinvite=1611209968917; _qddac=3-2-1.1.82r69m.kk6fbvh5; NLZT73369086lastvisitetime=1611210499311; NLZT73369086visitepages=45; NLZT73369086lastinvite=1611210502447; NLZT73369086LR_check_data=4%7C1611210502481%7C%7C%7C"
           }
proxies={"https": "http://222.37.125.107:32223", "http": "http://222.37.125.107:32223", }
domin="https://www.kcsjgcsw.com"
def generate_one(url):
    onelist = []
    # print("HelloWorldAndSpider!!!")
    try:
        res = r.get(url, headers=headers, proxies=proxies, verify=False)
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
        KK = input("请输入:")
        proxies["https"] = "http://" + KK
        proxies["http"] = "http://" + KK
        print(e)
        print(proxies["https"])
        # time.sleep(2)
        return generate_one(url)

if __name__ == '__main__':
    for x in urls:
        ss=generate_one(x)
        print(ss)



