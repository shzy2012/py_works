#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import logging
import random
import re
from dataclasses import dataclass
from datetime import datetime, timedelta

from tools.utils.constant import (
    MAX_AGE_YEAR,
    MIN_AGE_YEAR,
    ID_NUMBER_MATCHED_MSG,
    FEMALE,
    MALE
)
from tools.utils.pattern import ID_NUMBER_18_REGEX

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("./address.log")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


@dataclass(repr=False)
class IDMatchedData(object):
    id_number: str
    line: str
    address: str = ''
    birthday: str = ''
    age: int = 0
    sex: str = ''
    constellation: str = ''

    def __post_init__(self):
        id_number_util = IdNumber(self.id_number)
        self.address = id_number_util.get_area_name()
        self.age = id_number_util.get_age()
        self.sex = id_number_util.get_sex()
        self.constellation = id_number_util.get_constellation()
        self.birthday = id_number_util.get_birthday()

    def __str__(self):
        return ID_NUMBER_MATCHED_MSG.format(
            line=self.line,
            id_number=self.id_number,
            address=self.address,
            birthday=self.birthday,
            age=self.age,
            constellation=self.constellation,
            sex=self.sex
        )


class IDMatcher:
    def __init__(self):
        super().__init__()

    def process(self, data, line=1):
        """ 正则匹配输入字符串，并打印匹配值

        :param data: 待匹配的字符串
        :param line: 行号
        """
        # 1. 根据规则对输入进行正则匹配
        matched = self.match(data, line)

        # 2. 如果匹配到，依次输入匹配的内容
        for item in matched:
            print(item)

    @staticmethod
    def match(data, line):
        """

        :param data: 待匹配的字符串
        :param line: 行号
        :return:
        """
        result = []
        id_numbers = re.findall(ID_NUMBER_18_REGEX, data)
        for item in id_numbers:
            result.append(IDMatchedData(
                id_number=item[0],
                line=line
            ))
        return result


class IdNumber(object):

    address_code = {}

    def __init__(self, id):
        self.id = id
        self.area_id = int(self.id[0:6])
        self.birth_year = int(self.id[6:10])
        self.birth_month = int(self.id[10:12])
        self.birth_day = int(self.id[12:14])
        self._init()

    @classmethod
    def _init(cls):
        with open('data/address_code.json', encoding='utf-8') as f:
            cls.address_code = json.load(f)

    def get_area_name(self):
        """根据区域编号取出区域名称"""
        area_address = self.address_code.get(str(self.area_id))
        logger.info('地址是：%s' % area_address)
        return area_address

    def get_birthday(self):
        """通过身份证号获取出生日期"""
        if MIN_AGE_YEAR < self.birth_year < MAX_AGE_YEAR:
            return "{0}-{1}-{2}".format(
                self.birth_year, self.birth_month, self.birth_day)

    def get_age(self):
        """通过身份证号获取年龄"""
        now = (datetime.now() + timedelta(days=1))
        year, month, day = now.year, now.month, now.day

        if year == self.birth_year:
            return 0
        else:
            if self.birth_month > month or (
                    self.birth_month == month and self.birth_day > day):
                return year - self.birth_year - 1
            else:
                return year - self.birth_year

    def get_sex(self):
        """通过身份证号获取性别， 女生：0，男生：1"""
        sex = int(self.id[16:17]) % 2
        if sex == 1:
            return MALE
        else:
            return FEMALE

    def get_constellation(self):
        """通过身份证号获取星座"""

        if ((self.birth_month == 1 and self.birth_day > 19) or (self.birth_month == 2 and self.birth_day <= 18)):
            return "水瓶座"
        if ((self.birth_month == 2 and self.birth_day > 18) or (self.birth_month == 3 and self.birth_day <= 20)):
            return "双鱼座"
        if ((self.birth_month == 3 and self.birth_day > 20) or (self.birth_month == 4 and self.birth_day <= 19)):
            return "白羊座"
        if ((self.birth_month == 4 and self.birth_day > 19) or (self.birth_month == 5 and self.birth_day <= 20)):
            return "金牛座"
        if ((self.birth_month == 5 and self.birth_day > 20) or (self.birth_month == 6 and self.birth_day <= 21)):
            return "双子座"
        if ((self.birth_month == 6 and self.birth_day > 21) or (self.birth_month == 7 and self.birth_day <= 22)):
            return "巨蟹座"
        if ((self.birth_month == 7 and self.birth_day > 22) or (self.birth_month == 8 and self.birth_day <= 22)):
            return "狮子座"
        if ((self.birth_month == 8 and self.birth_day > 22) or (self.birth_month == 9 and self.birth_day <= 22)):
            return "处女座"
        if ((self.birth_month == 9 and self.birth_day > 22) or (self.birth_month == 10 and self.birth_day <= 23)):
            return "天秤座"
        if ((self.birth_month == 10 and self.birth_day > 23) or (self.birth_month == 11 and self.birth_day <= 22)):
            return "天蝎座"
        if ((self.birth_month == 11 and self.birth_day > 22) or (self.birth_month == 12 and self.birth_day <= 21)):
            return "射手座"
        if ((self.birth_month == 12 and self.birth_day > 21) or (self.birth_month == 1 and self.birth_day <= 19)):
            return "魔羯座"
        else:
            return None

    def get_check_digit(self):
        """通过身份证号获取校验码"""
        check_sum = 0
        for i in range(0, 17):
            check_sum += ((1 << (17 - i)) % 11) * int(self.id[i])
        check_digit = (12 - (check_sum % 11)) % 11
        return check_digit if check_digit < 10 else 'X'

    @classmethod
    def verify_last_number(cls, id):
        """校验身份证最后一位是否正确"""
        if len(id) == 18:
            check_digit = cls(id).get_check_digit()
            return str(check_digit) == id[-1]
        elif len(id) == 15:
            return True
        else:
            return False

    @classmethod
    def generate_id(cls, sex=0):
        """随机生成身份证号，sex = 0表示女性，sex = 1表示男性"""

        cls._init()

        # 随机生成一个区域码(6位数)
        id_number = str(random.choice(list(cls.address_code.keys())))
        # 限定出生日期范围(8位数)
        start, end = datetime.strptime("1960-01-01", "%Y-%m-%d"), datetime.strptime("2000-12-30", "%Y-%m-%d")
        birth_days = datetime.strftime(start + timedelta(random.randint(0, (end - start).days + 1)), "%Y%m%d")
        id_number += str(birth_days)
        # 顺序码(2位数)
        id_number += str(random.randint(10, 99))
        # 性别码(1位数)
        id_number += str(random.randrange(sex, 10, step=2))
        # 校验码(1位数)
        return id_number + str(cls(id_number).get_check_digit())


if __name__ == '__main__':
    """ 在项目 `py_works` 根目录执行 `python -m tools.ID` 测试 """

    random_sex = random.randint(0, 1)  # 随机生成男(1)或女(0)
    text = f'{IdNumber.generate_id(random_sex)}一刻也不能分割' \
           f'{IdNumber.generate_id(random_sex)}'
    print('文章是:', text)

    IDMatcher().process(text)
