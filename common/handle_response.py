

import jsonpath
from src.common.handle_data import EnvData


def extract_data_from_response(extract_exprs,response_dict):
    """
    根据jsonpath提取表达式，从响应结果当中，提取数据并设置为环境变量EnvData类的类属性，作为全局变量使用。
    :param extract_exprs: 从excel当中读取出来的，提取表达式的字符串。
    :param response_dict: http请求之后的响应结果。
    """
    # 将提取表达式转换成字典
    extract_dict = eval(extract_exprs)
    # 遍历字典，key作为全局变量名，value是jsonpath提取表达式。
    for key,value in extract_dict.items():
        # 提取
        res = str(jsonpath.jsonpath(response_dict,value)[0])
        # 设置环境变量
        setattr(EnvData,key,res)


if __name__ == '__main__':
    #ss为excel中的提取响应结果的表达式，response为响应结果，用此方法获取响应结果中的id作为全局环境变量
     ss = '{"id":"$..id","msg":"$..msg"}'
     response = {'code': 0, 'msg': 'success',
                 'data': {'id': 200713}}
     extract_data_from_response(ss,response)
     print(EnvData.__dict__)
