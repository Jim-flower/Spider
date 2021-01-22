import requests as r
import time
url ="http://ip.ipjldl.com/index.php/api/entry?method=proxyServer.hdtiqu_api_url&packid=0&fa=0&groupid=0&fetch_key=&time=102&qty=1&port=1&format=txt&ss=1&css=&dt=0&pro=&city=&usertype=4"
import telnetlib
def Work():
    ip = getIp()
    init = ip.split(":")
    one = init[0]
    two = init[-1]
    # print(one)
    # print(two)
    if testIp(one, two):
        return one+":"+str(int(two))
    else:
        return Work()

def testIp(one,two):
    try:
        telnetlib.Telnet(one, two, timeout=2)
        return 1
    except:
        return 0

def getIp():
    try:
        res = r.get(url)

        return res.text
    except Exception as e:
        time.sleep(1)

        return getIp()

if __name__ == '__main__':
    ip =Work()
    print(ip)





