from urllib import request

# 要访问的目标页面
targetUrl = "https://www.baidu.com"

# 代理服务器
proxyHost = "dyn.horocn.com"
proxyPort = "50000"

# 代理隧道验证信息
proxyUser = "隧道代理订单号"
proxyPass = "密码（用户中心-我的订单页面可查）"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyUser,
    "pass": proxyPass,
}

proxy_handler = request.ProxyHandler({
    "http": proxyMeta,
    "https": proxyMeta,
})

opener = request.build_opener(proxy_handler)

request.install_opener(opener)
resp = request.urlopen(targetUrl).read()

print(resp)