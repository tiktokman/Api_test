
import os
import unittest
import datetime
from BeautifulReport import BeautifulReport
#from common import config
#from common.handle_path import cases_dir,reports_dir
#发送邮件依赖包导入---

from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


if __name__ == '__main__':
    ##自动化用例存放文件夹
    cases_dir = os.path.join(os.getcwd(), r"TestCase")
    # 定义报告存放
    reports_dir = os.path.join(os.getcwd(), r"reports")
    #时间
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
    #报告名称
    reportName = 'krum_Test_Report_' + now + '.html'
    # 收集用例
    s = unittest.TestLoader().discover(cases_dir)

    # 生成报告
    br = BeautifulReport(s)
    br.report("鲸眼RUM测试报告",reportName,reports_dir)

    Subject = now+'鲸眼真实用户监测中心自动化测试结果'


    def sendMail(message, Subject, sender_show, recipient_show, to_addrs, cc_show=''):
        '''
        :param message: str 邮件内容
        :param Subject: str 邮件主题描述
        :param sender_show: str 发件人显示，不起实际作用如："xxx"
        :param recipient_show: str 收件人显示，不起实际作用 多个收件人用','隔开如："xxx,xxxx"
        :param to_addrs: str 实际收件人
        :param cc_show: str 抄送人显示，不起实际作用，多个抄送人用','隔开如："xxx,xxxx"
        '''
        # 填写真实的发邮件服务器用户名、密码
        user = 'jiewang@canway.net'
        password = '********'
        # 邮件内容
        msg = MIMEMultipart()
        msg.attach(MIMEText(message, 'html', _charset="utf-8"))
        # 构造附件1，传送当前目录下的 test.html文件
        att = MIMEText(open(reports_dir + "/" + reportName, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        # 附件名称为中文时的写法
        att.add_header("Content-Disposition", "attachment", filename=("utf-8", "", reportName))
        # 附件名称非中文时的写法,这里的filename可以任意写，写什么名字，邮件中显示什么名字
        # att["Content-Disposition"] = 'attachment; filename="{}"'.format(filename)
        msg.attach(att)
        # 邮件主题描述
        msg["Subject"] = Subject
        # 发件人显示，不起实际作用
        msg["from"] = sender_show
        # 收件人显示，不起实际作用
        msg["to"] = recipient_show
        # 抄送人显示，不起实际作用
        msg["Cc"] = cc_show
        with SMTP_SSL(host="smtp.exmail.qq.com", port=465) as smtp:
            # 登录发送邮件服务器
            smtp.login(user=user, password=password)
            # 实际发送、接收邮件配置
            smtp.sendmail(from_addr=user, to_addrs=to_addrs.split(','), msg=msg.as_string())
    if __name__ == '__main__':
        message = '''
               <p>jingyan_rum_testreport</p>
               <p>请各位查收鲸眼真实用户监测中心自动化测试结果！</p>
               '''  # 邮件内容
        sender = 'jiewang@canway.net'  # 显示发送人
        recipient = '******@qq.com'  # 实际发给的收件人
        #sendMail(message, Subject, sender, recipient, recipient, sender)
