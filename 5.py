import telnetlib
try:
    telnetlib.Telnet("123.73.82.42", "32223", timeout=2)
    print("代理IP有效！")
except:
    print("代理IP无效！")