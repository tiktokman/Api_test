
import json
from src.common import config
from src.common.handle_data import EnvData,clear_EnvData_attrs
from src.common.login import MySession
from src.common.handle_log import logger
class My_requests:

    #实例化一个持久会话对象
    def __init__(self,LOGIN_USER="",LOGIN_PASSWORD=""):

        self.session = MySession()
        self.session.login(LOGIN_USER,LOGIN_PASSWORD)

    def send_requests(self,method, url, data=None,token=None,**kwargs):
        """
        :param method:
        :param url:
        :param data:字典形式的数据。
        :return:
        """
        logger.info("发起一次HTTP请求")
        # 得到请求头
        headers = {"Referer": config.RefererUrl,
                   "Content-Type": "application/json"}
        headers["X-CSRFToken"] = EnvData.bk_csrftoken
        #print(EnvData.bk_csrftoken)
        # 请求数据的处理 - 如果是字符串，则转换成字典对象。
        if data is not None and isinstance(data, str):
            # 如果有null，则替换为None
            if data.find("null") != -1:
                data = data.replace("null", "None")
            # 使用eval转成字典.eval过程中，如果表达式有涉及计算，会自动计算。
            false = False
            true = True
            null = ''
            data = eval(data)
        # 将请求数据转换成字典对象。
        logger.info("请求头为：{}".format(headers))
        logger.info("请求方法为：{}".format(method))
        logger.info("请求url为：{}".format(url))
        logger.info("请求数据为：{}".format(data))
        # 根据请求类型，调用请求方法
        method = method.upper()  # 大写处理
        if method == "GET":
            resp = self.session.request(method,url, data, headers=headers, verify=False)
        elif method == "POST":
            resp = self.session.request(method,url, json=data, headers=headers, verify=False)
        elif method == "PUT":
            resp = self.session.request(method,url, json=data, headers=headers, verify=False)
        elif method == "PATCH":
            resp = self.session.request(method,url,json=data,headers=headers,verify=False)
        else:
            resp = self.session.request(method,url, data, headers=headers, verify=False)
        logger.info("响应状态码为：{}".format(resp.status_code))
        logger.info("响应数据为：{}".format(json.loads(resp.text)))
        return resp
    def upload_file(self,method, url, data=None,files=None,token=None,**kwargs):
        logger.info("发起一次HTTP请求")
        # 得到请求头
        headers = {"Referer": config.RefererUrl
                   #,"Content-Type": "application/json"   #content-type参数，如果我们通过form-data的方式上传文件，我们发送post请求的时候，headers这个参数中一定不能要包括这个值，即上传文件不需要加content-type，requests库会自动添加这个header字段
                   }
        headers["X-CSRFToken"] = EnvData.bk_csrftoken

        logger.info("请求头为：{}".format(headers))
        logger.info("请求方法为：{}".format(method))
        logger.info("请求url为：{}".format(url))
        logger.info("请求数据为：{}".format(data))
        # 根据请求类型，调用请求方法
        method = method.upper()  # 大写处理
        if method == "GET":
            resp = self.session.request(method,url, data, headers=headers, verify=False)
        elif method == "POST":
            resp = self.session.request(method,url, files=files,headers=headers, verify=False)
        else:
            resp = self.session.request(method,url, data, headers=headers, verify=False)
        logger.info("响应状态码为：{}".format(resp.status_code))
        logger.info("响应数据为：{}".format(json.loads(resp.text)))
        return resp



def __handle_header(token=None):
    """
            处理请求头。加上项目当中必带的请求头。如果有token，加上token。
            :param token: token值EnvData.bk_csrftoken
            :return: 处理之后headers字典
            """
    headers = {"Referer": config.RefererUrl,
               "Content-Type": "application/json"}
    if token:
        headers["X-csrfToken"] = token
    return headers


def __pre_data(data):
    """
            如果data是字符串，则转换成字典对象。
            """
    if data is not None and isinstance(data, str):
        # 如果有null，则替换为None
        if data.find("null") != -1:
            data = data.replace("null", "None")
        # 使用eval转成字典.eval过程中，如果表达式有涉及计算，会自动计算。
        data = eval(data)
    return data








