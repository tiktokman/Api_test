
import re
import json
import random

class EnvData:
    """
    存储用例要使用到的数据。
    """
    mytest = "testattr"

def clear_EnvData_attrs():
    # 清理 EnvData里设置的属性
    values = dict(EnvData.__dict__.items())
    for key, value in values.items():
        if key.startswith("__"):
            pass
        else:
            delattr(EnvData, key)


def replace_case_by_regular(case):
    """
    对excel当中，读取出来的整条测试用例，做全部替换。
    包括url,request_data
    """
    for key,value in case.items():
        if value is not None and isinstance(value, str):  # 确保是个字符串
            case[key] = replace_by_regular(value)
    return case

def replace_by_regular(data):
    """
    将字符串当中，匹配#(.*?)#部分，替换对应的真实数据。
    data: 字符串
    return: 返回的是替换之后的字符串
    ps： EvnData的类属性,必须都是字符串类型。
    """
    res = re.findall("#(.*?)#", data)  # 如果没有找到，返回的是空列表。
    if res:
        for item in res:
            # 得到标识符对应的值。
            try:
                value = getattr(EnvData, item)
            except AttributeError:
                # value = "#{}#".format(item)
                continue
            print(value)
            # 再去替换原字符串
            data = data.replace("#{}#".format(item), value)
    return data


def replace_mark_with_data(case,mark,real_data):
    """
    case: excel当中读取出来一条数据。是个字典。
    mark: 数据当中的占位符。#值
    real_data: 要替换mark的真实数据。
    """
    #遍历一个http请求用例涉及到的所有数据，如果说每一个数据有需要替换的，都会替换。
    for key,value in case.items():
        if value is not None and isinstance(value,str): # 确保是个字符串
            if value.find(mark) != -1: # 找到标识符
                #print(key,value,"123")
                case[key] = value.replace(mark,real_data)
    return case


def get_new_data(data=None):
    newdata = "RUMautotest"  #固定前缀
    for _ in range(0,6): # 生成后6位
        newdata += str(random.randint(0,7))
    if data:
        newdata += data
    return newdata






if __name__ == '__main__':
    case = {
        "method": "POST#id#",
        "url": "http://www.#baidu#.com",
        "request_data": '{"id": "#id#", "pwd": "123456789","userinfo":{"user_id": "#id#","user_name"：“Jack”}}'
    }
    if case["request_data"].find("#id#") != -1:
        case = replace_mark_with_data(case, "#id#", "1234567")
    for key,value in case.items():
        print(key,value)
