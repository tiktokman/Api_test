import csv

import unittest
import json
from src.common.handle_data import EnvData,clear_EnvData_attrs,replace_mark_with_data,get_new_data
from src.common.handle_path import datas_dir
from src.common.handle_requests import My_requests
from src.common import config
import jsonpath
from src.common.handle_log import logger

filename = datas_dir+"\\rum_test.csv"

cases = []
with open(filename,newline='') as csvfile:
    reader=csv.DictReader(csvfile)  #将文件读取为dict对象，无法索引访问
    #遍历reader，转化为列表case存储dict，这样便可使用索引访问
    for i in reader:
        cases.append(i)

#实例化存储过程数据的对象
EnvData = EnvData()

#登录admin,获取一个带登录信息的持久化会话对象
admin= My_requests("jiewang@cwdev.net","Wang622616")


class NewApplication(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        logger.info("************** 创建应用接入探针场景 开始测试 ************")

    @classmethod
    def tearDownClass(cls) -> None:
        """
        if EnvData.NewNode_id :
            sql1 = config.sql_delete_task_node_V3("#参数",EnvData.NewNode_id)
            sql2 = config.sql_delete_task_node_kmc("#参数",EnvData.NewNode_id)
            db2.update(sql1)
            db3.update(sql2)
        if EnvData.Task_name or EnvData.AmendTask_name:
            sql3 = config.sql_delete_task_V3("#参数",EnvData.Task_name)
            sql4 = config.sql_delete_task_V3("#参数",EnvData.AmendTask_name)
        """
        logger.info("************** 创建应用接入探针场景 结束测试 ************")

    def test01_Create_Application(self):
        NewApplication_name = get_new_data()
        setattr(EnvData,"NewApplication_name",NewApplication_name)
        case01 = replace_mark_with_data(cases[0],"#应用名称",NewApplication_name)
        logger.info("*********   执行用例{}：{}   *********".format(case01["编号"],case01["用例名称"]))
        result = admin.send_requests(method=case01["请求方式"],
                                               url=config.Base_Url+case01["url"],
                                               data=case01["请求参数"],
                                               headers=case01["headers"])
        result = json.loads(result.text)

        try:
            assert result["result"] == True
            print("用例通过：{}\n请求参数：{}\n响应参数：{}".format(case01["用例名称"], case01["请求参数"], result))
        except Exception as e:
            print("用例不通过：{}\n请求参数：{}\n响应参数：{}".format(case01["用例名称"], case01["请求参数"], result))
            self.assertFalse(e)

    def test02_Application_list(self):
        case02 = cases[1]
        logger.info("*********   执行用例{}：{}   *********".format(case02["编号"], case02["用例名称"]))
        result = admin.send_requests(method=case02["请求方式"],
                               url=config.Base_Url+case02["url"],
                               data=case02["请求参数"],
                               headers=case02["headers"])
        result = json.loads(result.text)

        NewApplication_id = str(jsonpath.jsonpath(result,"$..data[*].application_id")[0])
        setattr(EnvData,"NewApplication_id",NewApplication_id)

        try:
            assert result["result"] == True
            #print(jsonpath.jsonpath(result,"$..data[*].application_name"))
            self.assertIn(EnvData.NewApplication_name,jsonpath.jsonpath(result,"$..data[*].application_name"))
            print("用例通过：{}\n请求参数：{}\n响应参数：{}".format(case02["用例名称"], case02["请求参数"], result))
        except Exception as e:
            print("用例不通过：{}\n请求参数：{}\n响应参数：{}".format(case02["用例名称"], case02["请求参数"], result))
            self.assertFalse(e)

    def test03_js_link_info(self):
        case03 = replace_mark_with_data(cases[2],"#应用id",EnvData.NewApplication_id)

        logger.info("*********   执行用例{}：{}   *********".format(case03["编号"], case03["用例名称"]))
        result = admin.send_requests(method=case03["请求方式"],
                               url=config.Base_Url+case03["url"],
                               data=case03["请求参数"],
                               headers=case03["headers"])
        result = json.loads(result.text)

        try:
            assert result["result"] == True
            print("用例通过：{}\n请求参数：{}\n响应参数：{}".format(case03["用例名称"], case03["请求参数"], result))
        except Exception as e:
            print("用例不通过：{}\n请求参数：{}\n响应参数：{}".format(case03["用例名称"], case03["请求参数"], result))
            self.assertFalse(e)

    def test04_upload_Confoundfile(self):
        case04 = replace_mark_with_data(cases[3],"#应用id",EnvData.NewApplication_id)
        case04 = replace_mark_with_data(case04,"#应用名称",EnvData.NewApplication_name)

        files = {'confound_file':('web_react_js_map_03.zip',open('..\TestDatas\web_react_js_map_03.zip', 'rb'),'application/x-zip-compressed')}
        #files = {'confound_file': ('web_react_js_map_03.zip', open('TestDatas\web_react_js_map_03.zip', 'rb'), 'application/x-zip-compressed')}  #根据调用执行路径，确定文件相对路径，这里为all_test调用
        logger.info("*********   执行用例{}：{}   *********".format(case04["编号"], case04["用例名称"]))
        result = admin.upload_file(method=case04["请求方式"],
                               url=config.Base_Url+case04["url"],
                               files=files,
                               headers=case04["headers"])
        result = json.loads(result.text)

        try:
            assert result["result"] == True
            #print(jsonpath.jsonpath(result,"$..data[*].application_name"))
            print("用例通过：{}\n请求参数：{}\n响应参数：{}".format(case04["用例名称"], case04["请求参数"], result))
        except Exception as e:
            print("用例不通过：{}\n请求参数：{}\n响应参数：{}".format(case04["用例名称"], case04["请求参数"], result))
            self.assertFalse(e)


    def test05_Insert_Probe(self):
        case05 = replace_mark_with_data(cases[4],"#应用id",EnvData.NewApplication_id)
        case05 = replace_mark_with_data(case05,"#应用名称",EnvData.NewApplication_name)

        logger.info("*********   执行用例{}：{}   *********".format(case05["编号"], case05["用例名称"]))
        result = admin.send_requests(method=case05["请求方式"],
                               url=config.Base_Url+case05["url"],
                               #url=config.local_dev_Url+case05["url"],
                               data=case05["请求参数"],
                               headers=case05["headers"])
        result = json.loads(result.text)

        try:
            assert result["result"] == True
            #print(jsonpath.jsonpath(result,"$..data[*].application_name"))
            print("用例通过：{}\n请求参数：{}\n响应参数：{}".format(case05["用例名称"], case05["请求参数"], result))
        except Exception as e:
            print("用例不通过：{}\n请求参数：{}\n响应参数：{}".format(case05["用例名称"], case05["请求参数"], result))
            self.assertFalse(e)

    def test06_Delete_Application(self):
        case06 = replace_mark_with_data(cases[5],"#应用id",EnvData.NewApplication_id)
        case06 = replace_mark_with_data(case06,"#应用名称",EnvData.NewApplication_name)

        logger.info("*********   执行用例{}：{}   *********".format(case06["编号"], case06["用例名称"]))
        result = admin.send_requests(method=case06["请求方式"],
                               url=config.Base_Url+case06["url"],
                               #url=config.local_dev_Url+case05["url"],
                               data=case06["请求参数"],
                               headers=case06["headers"])
        result = json.loads(result.text)

        try:
            assert result["result"] == True
            #print(jsonpath.jsonpath(result,"$..data[*].application_name"))
            print("用例通过：{}\n请求参数：{}\n响应参数：{}".format(case06["用例名称"], case06["请求参数"], result))
        except Exception as e:
            print("用例不通过：{}\n请求参数：{}\n响应参数：{}".format(case06["用例名称"], case06["请求参数"], result))
            self.assertFalse(e)

if __name__ == '__main__':
    s = NewApplication()
