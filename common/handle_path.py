import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print(base_dir)
# 测试用例路径
cases_dir = os.path.join(base_dir,"TestCase")
#print(cases_dir)
# 测试数据的路径
datas_dir = os.path.join(base_dir,"TestDatas")
# 测试报告
reports_dir = os.path.join(base_dir,"reports")
# 日志的路径
logs_dir = os.path.join(base_dir,"log")
# 配置文件路径
conf_dir = os.path.join(base_dir,"common")

