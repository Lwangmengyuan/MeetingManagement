# _*_conding:utf-8_*_
# 作者: 杨佳
# 创建时间: 2020/5/14 20:09
# 文件: log
import logging
import os
from common.setting import Settings


class RecordLog:

    def __init__(self, name=None):
        s = Settings()
        #  设置一个日志器
        if name is None:
            self.logger = logging.getLogger('日志记录')
        else:
            self.logger = logging.getLogger(name)
        #  设置日志器的最低记录等级
        self.logger.setLevel(logging.DEBUG)

        #  设置控制台日志(在控制台打印的日志)
        console_log = logging.StreamHandler()
        #  设置控制台打印日志的等级
        console_log.setLevel(logging.INFO)
        #  设置保存为文件日志的名字
        name = s.base_name
        #  设置文件日志(保存为文件的日志)，文件日志的默认等级为日志器的等级
        file_log = logging.FileHandler(s.log_path + name + '.log', encoding='utf-8')
        #  设置打印的格式
        formatter = logging.Formatter("[%(levelname)s]:[%(filename)s]-[%(funcName)s]:%(lineno)d %(message)s")
        console_log.setFormatter(formatter)
        file_log.setFormatter(formatter)
        #  将控制台日志和文件日志添加进入日志器
        self.logger.addHandler(console_log)
        self.logger.addHandler(file_log)

    def get_log(self):
        return self.logger


do_log = RecordLog().get_log()

if __name__ == '__main__':
    do_log.info('记录日志')
    do_log.error('错误日志')
    do_log.warning('警告日志')
