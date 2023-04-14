
from src.common import config
from requests import Session
from jsonpath import jsonpath
import re
import json
from src.common.handle_data import EnvData,clear_EnvData_attrs


class MySession(Session):   # 继承python的Session基类，使用它的所有方法，再把我们需要的cookie、hearders值传进去


    def __init__(self):
        super().__init__()
    Url = config.Base_Url
    SaaSUrl = Url + config.SaaS_Url

    # 获取登录的bk_token

    def get_bk_token(self) -> str:
        # csrf模式下先发get请求，获取bklogin_csrftoken，再用post请求，把bklogin_csrftoken放在data里
        headers = self.get(url=self.SaaSUrl,verify=False).headers

        bk_token = ((re.compile("ftoken=(.*?); expires")).findall(str(headers)))[0]
        return bk_token


    # 用户登陆
    def login(self,LOGIN_USER,LOGIN_PASSWORD):
        clear_EnvData_attrs()
        bk_token = self.get_bk_token()
        param = {
            "csrfmiddlewaretoken": bk_token,
            "username": LOGIN_USER,
            "password": LOGIN_PASSWORD
        }
        header = {
            "Referer": self.SaaSUrl,
            "User-Agent": config.User_Agent
        }
        #urllib3.disable_warnings()
        print(header)
        res = self.post(url=self.SaaSUrl, data=param,verify=False,headers=header).headers
        #kingeye_web_saas_sessionid = ((re.compile("kingeye-web_saas_sessionid=(.*?); expires")).findall(str(res)))[0]
        bk_csrftoken =((re.compile("csrftoken=(.*?); expires")).findall(str(res)))[0]#获取登录的bklogin_csrftoken
        #sessionid = ((re.compile("sessionid=(.*?); expires")).findall(str(res)))[0]
        #bk_token = ((re.compile("bk_token=(.*?); Domain=")).findall(str(res)))[0]
        #print(res)
        #设置环境变量
        setattr(EnvData, "bk_csrftoken", bk_csrftoken)

        #访问krum地址，获取相关的cookie（很神奇，不知道为啥直接访问这个之后，就可以完成鉴权了，也没做其他操作，也没提取cookie）
        res = self.get(url=config.Krum_SaaS_Url,  verify=False, headers=header).headers

        print("我登陆了。。。。。")
        return bk_csrftoken

if __name__ == '__main__':
    s = MySession()
    #print(s)



