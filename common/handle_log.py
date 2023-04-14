
import logging
import os
import datetime   # 时间模块
from src.common import config
from src.common.handle_path import logs_dir

class MyLogger(logging.Logger):

    def __init__(self,file=None):
        # 设置输出级别、输出渠道、输出日志格式
        # super().__init__(name,level)
        super().__init__(config.logname,config.log_level)

        # 日志格式
        fmt = '%(asctime)s %(name)s %(levelname)s %(filename)s-%(lineno)d line：%(message)s'
        formatter = logging.Formatter(fmt)

        # 控制台渠道
        handle1 = logging.StreamHandler()
        handle1.setFormatter(formatter)
        self.addHandler(handle1)

        if file:
            # 文件渠道
            handle2 = logging.FileHandler(file,encoding="utf-8")
            handle2.setFormatter(formatter)
            self.addHandler(handle2)
#获取当前时间
now = datetime.datetime.now().strftime('%Y-%m-%d_%H')
# 获取今天的日期
#today_date = str(datetime.date.today())
# 是否需要写入文件
#if config.getboolean(config.logfile_ok):
file_name = os.path.join(logs_dir,now+config.logfilename)
#else:
    #file_name = None


logger = MyLogger(file_name)

# logger.info("1111111111111111")
