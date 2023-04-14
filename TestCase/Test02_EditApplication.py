
import unittest
from src.common.handle_excel import HandleExcel
import json
from src.common.handle_data import EnvData,clear_EnvData_attrs,replace_mark_with_data,get_new_data
from src.common.handle_path import datas_dir
from src.common.handle_db import HandleDB1
from src.common.handle_requests import My_requests
from src.common import config
import jsonpath
from src.common.handle_log import logger

#导入excel,获取其中数据
he = HandleExcel(datas_dir+"\\rum测试用例.xlsx","应用配置编辑")
#cases列表存储工作表下所有用例
cases = he.read_all_datas()
he.close_file()

#实例化存储过程数据的对象
EnvData = EnvData()

#登录admin,获取一个带登录信息的持久化会话对象
admin= My_requests("jiewang@cwdev.net","Wang622616")


class EditApplication(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        logger.info("************** 应用配置编辑场景 开始测试 ************")


    @classmethod
    def tearDownClass(cls) -> None:

        logger.info("************** 应用配置编辑场景 结束测试 ************")

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

        NewApplication_id = str(jsonpath.jsonpath(result,"$.data.application_id")[0])
        setattr(EnvData,"NewApplication_id",NewApplication_id)
        try:
            assert result["result"] == True
            print("用例通过：{}\n请求参数：{}\n响应参数：{}".format(case01["用例名称"], case01["请求参数"], result))
        except Exception as e:
            print("用例不通过：{}\n请求参数：{}\n响应参数：{}".format(case01["用例名称"], case01["请求参数"], result))
            self.assertFalse(e)

    def test02_upload_Confoundfile(self):
        case02 = replace_mark_with_data(cases[1],"#应用id",EnvData.NewApplication_id)
        case02 = replace_mark_with_data(case02,"#应用名称",EnvData.NewApplication_name)

        #files = {'confound_file':('web_react_js_map_03.zip',open('..\TestDatas\web_react_js_map_03.zip', 'rb'),'application/x-zip-compressed')}
        files = {'confound_file': ('web_react_js_map_03.zip', open('TestDatas\web_react_js_map_03.zip', 'rb'), 'application/x-zip-compressed')}  #根据调用执行路径，确定文件相对路径，这里为all_test调用

        logger.info("*********   执行用例{}：{}   *********".format(case02["编号"], case02["用例名称"]))
        result = admin.upload_file(method=case02["请求方式"],
                               url=config.Base_Url+case02["url"],
                               files=files,
                               headers=case02["headers"])
        result = json.loads(result.text)

        #获取反混淆文件id,转成字符串，去掉首位方括号[]
        confoundfile_id = str(jsonpath.jsonpath(result,"$.data.confound_file_id")).strip("[").strip("]")
        setattr(EnvData,"confoundfile_id",confoundfile_id)

        try:
            assert result["result"] == True
            print("用例通过：{}\n请求参数：{}\n响应参数：{}".format(case02["用例名称"], case02["请求参数"], result))
        except Exception as e:
            print("用例不通过：{}\n请求参数：{}\n响应参数：{}".format(case02["用例名称"], case02["请求参数"], result))
            self.assertFalse(e)


    def test03_Insert_Probe(self):
        case03 = replace_mark_with_data(cases[2],"#应用id",EnvData.NewApplication_id)
        case03 = replace_mark_with_data(case03,"#应用名称",EnvData.NewApplication_name)

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

    def test04_Check_allow(self):
        case04 = replace_mark_with_data(cases[3],"#应用id",EnvData.NewApplication_id)

        logger.info("*********   执行用例{}：{}   *********".format(case04["编号"], case04["用例名称"]))
        result = admin.send_requests(method=case04["请求方式"],
                               url=config.Base_Url+case04["url"],
                               data=case04["请求参数"],
                               headers=case04["headers"])
        result = json.loads(result.text)

        try:
            assert result["result"] == True
            print("用例通过：{}\n请求参数：{}\n响应参数：{}".format(case04["用例名称"], case04["请求参数"], result))
        except Exception as e:
            print("用例不通过：{}\n请求参数：{}\n响应参数：{}".format(case04["用例名称"], case04["请求参数"], result))
            self.assertFalse(e)

    def test05_Edit_Appilication(self):
        case05 = replace_mark_with_data(cases[4],"#应用id",EnvData.NewApplication_id)

        NewApplication_name = get_new_data("编辑名称")
        setattr(EnvData,"NewApplication_name",NewApplication_name)
        case05 = replace_mark_with_data(case05,"#应用名称",EnvData.NewApplication_name)
        case05 = replace_mark_with_data(case05, "#编辑名称", EnvData.NewApplication_name)

        logger.info("*********   执行用例{}：{}   *********".format(case05["编号"], case05["用例名称"]))
        result = admin.send_requests(method=case05["请求方式"],
                               url=config.Base_Url+case05["url"],
                               data=case05["请求参数"],
                               headers=case05["headers"])
        result = json.loads(result.text)

        try:
            assert result["result"] == True
            print("用例通过：{}\n请求参数：{}\n响应参数：{}".format(case05["用例名称"], case05["请求参数"], result))
        except Exception as e:
            print("用例不通过：{}\n请求参数：{}\n响应参数：{}".format(case05["用例名称"], case05["请求参数"], result))
            self.assertFalse(e)

    def test06_Audit_List(self):
        case06 = replace_mark_with_data(cases[5],"#应用id",EnvData.NewApplication_id)

        logger.info("*********   执行用例{}：{}   *********".format(case06["编号"], case06["用例名称"]))
        result = admin.send_requests(method=case06["请求方式"],
                               url=config.Base_Url+case06["url"],
                               data=case06["请求参数"],
                               headers=case06["headers"])
        result = json.loads(result.text)

        try:
            assert result["result"] == True
            print("用例通过：{}\n请求参数：{}\n响应参数：{}".format(case06["用例名称"], case06["请求参数"], result))
        except Exception as e:
            print("用例不通过：{}\n请求参数：{}\n响应参数：{}".format(case06["用例名称"], case06["请求参数"], result))
            self.assertFalse(e)

    def test07_Edit_Perf(self):
        case07 = replace_mark_with_data(cases[6],"#应用id",EnvData.NewApplication_id)
        case07 = replace_mark_with_data(cases[6], "#应用名称", EnvData.NewApplication_name)

        logger.info("*********   执行用例{}：{}   *********".format(case07["编号"], case07["用例名称"]))
        result = admin.send_requests(method=case07["请求方式"],
                               url=config.Base_Url+case07["url"],
                               data=case07["请求参数"],
                               headers=case07["headers"])
        result = json.loads(result.text)

        try:
            assert result["result"] == True
            print("用例通过：{}\n请求参数：{}\n响应参数：{}".format(case07["用例名称"], case07["请求参数"], result))
        except Exception as e:
            print("用例不通过：{}\n请求参数：{}\n响应参数：{}".format(case07["用例名称"], case07["请求参数"], result))
            self.assertFalse(e)

    def test08_Delete_Confoundfile(self):
        case08 = replace_mark_with_data(cases[7],"#应用id",EnvData.NewApplication_id)
        case08 = replace_mark_with_data(cases[7],"#file_id",EnvData.confoundfile_id)
        case08 = replace_mark_with_data(cases[7],"#应用名称",EnvData.NewApplication_name)


        logger.info("*********   执行用例{}：{}   *********".format(case08["编号"], case08["用例名称"]))
        result = admin.send_requests(method=case08["请求方式"],
                               url=config.Base_Url+case08["url"],
                               data=case08["请求参数"],
                               headers=case08["headers"])
        result = json.loads(result.text)

        try:
            assert result["result"] == True
            print("用例通过：{}\n请求参数：{}\n响应参数：{}".format(case08["用例名称"], case08["请求参数"], result))
        except Exception as e:
            print("用例不通过：{}\n请求参数：{}\n响应参数：{}".format(case08["用例名称"], case08["请求参数"], result))
            self.assertFalse(e)

if __name__ == '__main__':
    s = EditApplication()
