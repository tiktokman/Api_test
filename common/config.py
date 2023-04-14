
#登录URL,username,password
'''
Base_Url = "https://paas.stress.com"   #stress测试环境
LOGIN_USER = "admin"
LOGIN_PASSWORD = "canway2021"

#stress环境开发者中心直接进入鲸眼SaaS的o环境
#SaaS_Url = "/login/?c_url=https%3A//paas.stress.com/o/kingeye-web_saas/&app_code=kingeye-web_saas#/home"
SaaS_Url = "/login/?c_url=/console/"
User_Agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"

RefererUrl = "https://paas.stress.com/o/kingeye-web_saas/"  #stress测试环境

Krum_SaaS_Url = "https://paas.stress.com/o/krum_saas/api/v1/krum/"

'''
Base_Url = "http://paas.test.com"   #stress测试环境
LOGIN_USER = "jiewang@cwdev.net"
LOGIN_PASSWORD = "Wang622616"

#stress环境开发者中心直接进入鲸眼SaaS的o环境
SaaS_Url = "/login/?c_url=/console/"

User_Agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"

RefererUrl = "http://paas.test.com/o/kingeye-web_saas/"

Krum_SaaS_Url = "http://paas.test.com/o/krum_saas/api/v1/krum/"


import datetime
import time

#开始毫秒时间戳
begin_time = round((datetime.datetime.now()-datetime.timedelta(days=30)).timestamp()*1000)
#七天前毫秒时间戳
end_time = round(time.time()*1000)




#近一个小时的时间范围
timerange = str((datetime.datetime.now()-datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:%M")) + "--" +str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
Before_hour_time = str((datetime.datetime.now()-datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S"))
nowtime = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
timestamp = int(round(time.time() * 1000))
#print(timerange)
#日志配置信息
logname = "krum_log"
log_level = "INFO"
logfile_ok = True
logfilename = "jingyan_rum_log"

#数据库配置信息
db_host = "10.11.25.61"
db_port = 3306
db_user = "root"
db_password = "canway2021"
db_database1 = "bkmonitorv3_alert"
db_database2 = "bk_monitorv3"
db_database3 = "kmc_saas"

# sql语句查询监控平台策略
sql_alarm_strategy = 'select count(*) from alarm_strategy_v2 where alarm_strategy_v2.`name` like "#参数%"'
#拨测任务删除失败时，清除平台与监控中心的脏数据
sql_delete_task_node_V3 = " DELETE FROM monitor_uptimechecktask_nodes WHERE uptimechecktask_id = #参数 "
sql_delete_task_V3 = " DELETE FROM monitor_uptimechecktask WHERE name = #参数 "
sql_delete_node_V3 = " DELETE FROM monitor_uptimechecknode WHERE name = #参数 "

sql_delete_task_node_kmc = " DELETE FROM monitor_uptimechecktask_nodes WHERE uptimechecktask_id = #参数 "
sql_delete_task_kmc = " DELETE FROM monitor_uptimechecktask WHERE name = #参数 "
sql_delete_node_kmc = " DELETE FROM monitor_uptimechecknode WHERE name = #参数 "



#邮箱配置信息
message = '''
       <p>jingyan_krum_testreport</p>
       <p>请各位查收鲸眼真实用户监测中心自动化测试结果！</p>
       ''' #邮件内容
sender = 'jiewang@canway.net'# 显示发送人
recipient = '504888954@qq.com'# 实际发给的收件人


#时序上报shell命令
ssh_ip = "192.168.163.123"
ssh_username = "root"
ssh_password = "PAScanway2022"
ssh_port = 22
cmd_1 = "/usr/local/gse_stress/plugins/bin"
cmd_2 = "./bkmonitorbeat -report -report.bk_data_id 1503253 -report.type agent -report.message.kind timeseries -report.message.body '{'data_id': 1503253,'access_token': 'eebef96465194696a666dfd32dfce9d3','data': [{'metrics': {'cpu_load': 234},'timestamp':1671107156000,'target': '127.0.1.3','dimension': {'bk_obj_id': 'host','cpu': 'cpu1'}}]}'"