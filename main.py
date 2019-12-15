#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
文件匹配地址、手机号、身份证号

1. 如果没有传入文件路径，指定默认的文件
2. 判断输入文件大小是否合法。如果不合法，给出提示后退出。
3. 创建任务，依次匹配地址、手机号、身份证号
"""

import os
import sys

from tools.ID import ID
from tools.address import AddressMatcher
from tools.phone import PhoneMatcher
from tools.task import Task
from tools.utils import constant


class FileMatcher(object):

    def __init__(self):
        self.address_matcher = AddressMatcher()
        self.phone_matcher = PhoneMatcher()
        self.id_matcher = ID()

    @staticmethod
    def is_file_size_valid(file_path):
        """ 文件大小是否合法

        :param file_path: 文件路径
        :return:
        """
        return os.path.getsize(file_path) <= constant.FILE_MAX_SIZE

    def match(self, file_path: str = ''):
        """ 匹配文件中的地址、手机号、身份证号

        :param file_path: 文件路径
        :return:
        """
        # 1. 如果没有传入文件路径，指定默认的文件
        if not file_path:
            file_path = os.getcwd() + '/data/data1.txt'

        # 2. 判断输入文件大小是否合法。如果不合法，给出提示后退出。
        if not self.is_file_size_valid(file_path):
            print(constant.FILE_SIZE_INVALID_MSG)
            return

        # 3. 创建任务，依次匹配地址、手机号、身份证号
        task = Task()
        task.add_works(self.address_matcher.process)\
            .add_works(self.phone_matcher.process)\
            .add_works(self.id_matcher.Do)\
            .process(file_path)


if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else ''
    FileMatcher().match(path)
