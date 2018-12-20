import time
import requests
def isConnected():
    try:
        html=requests.get("https://www.baidu.com/",timeout=2)
    except:
        return False
    return True
def run():
    while 1:
        networkStatus = isConnected()
        if networkStatus == False:
            address ="http://a.nuist.edu.cn/index.php/index/login"
            head={
                'Accept':'application/json, text/javascript, */*; q=0.01',
                'Accept-Encoding':'gzip, deflate',
                'gzip, deflate':'zh-CN,zh;q=0.9',
                'Connection':'keep-alive',
                'Content-Length':'66',
                'Content-Type':'application/x-www-form-urlencoded',
                'Cookie':'sunriseUsername=18851777935; sunriseDomain=CMCC; sunriseRememberPassword=true; sunrisePassword=097812; UM_distinctid=164eb4d02714f7-05d2937542e30b-2711938-100200-164eb4d0272130; think_language=zh-CN; PHPSESSID=40r6e79ako5fbs2c8q82vk7rj3',
                'Host':'a.nuist.edu.cn',
                'Origin':'http://a.nuist.edu.cn',
                'Referer':'http://a.nuist.edu.cn/',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
                'X-Requested-With':'XMLHttpRequest'
            }
            LoginData={'username':'18851777935',
                       'domain':'CMCC',
                       'password':'MDk3ODEy',
                       'enablemacauth':'0'
            }
            result=requests.post(address,data=LoginData,headers=head)
            time.sleep(600)
run()
