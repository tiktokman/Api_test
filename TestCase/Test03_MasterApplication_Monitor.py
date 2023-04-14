
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
he = HandleExcel(datas_dir+"\\rum测试用例.xlsx","主站数据接口监控")
#cases列表存储工作表下所有用例
cases = he.read_all_datas()
he.close_file()


#实例化存储过程数据的对象
EnvData = EnvData()

#登录admin,获取一个带登录信息的持久化会话对象
admin= My_requests("jiewang@cwdev.net","Wang622616")

class MasterApplication(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        logger.info("************** 主站数据接口监控场景 开始测试 ************")


    @classmethod
    def tearDownClass(cls) -> None:

        logger.info("************** 主站数据接口监控场景 结束测试 ************")

    def test01_RunOverview(self):

        case01 = replace_mark_with_data(cases[0],"#start",str(config.begin_time))
        case01 = replace_mark_with_data(cases[0],"#end",str(config.end_time))
        '''
        当接口校验参数值类型的时候，如判断时间是否为int型，字符串无法直接替换为int，需要用以下方法将str转为json，再做替换
        
        case01 = cases[0]
        case01["请求参数"] = json.loads(case01["请求参数"])
        print(type(case01["请求参数"]))

        for objs in case01["请求参数"]:
            if "ts_begin" == objs:
                case01["请求参数"]["ts_begin"] = config.begin_time
        for objs in case01["请求参数"]:
            if "ts_end" == objs:
                case01["请求参数"]["ts_end"] = config.end_time
        '''
        logger.info("*********   执行用例{}：{}   *********".format(case01["编号"],case01["用例名称"]))
        result = admin.send_requests(method=case01["请求方式"],
                                               url=config.Base_Url+case01["url"],
                                               data=case01["请求参数"],
                                               headers=case01["headers"])
        result = json.loads(result.text)
        total = jsonpath.jsonpath(result,"$.data.total")

        try:
            assert result["result"] == True
            self.assertEqual(total,[1])
            print("用例通过：{}\n请求参数：{}\n响应参数：{}".format(case01["用例名称"], case01["请求参数"], result))
        except Exception as e:
            print("用例不通过：{}\n请求参数：{}\n响应参数：{}".format(case01["用例名称"], case01["请求参数"], result))
            self.assertFalse(e)

if __name__ == '__main__':
    s = MasterApplication()
