#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
号码匹配:
1. 根据规则对输入进行正则匹配
    1.1 判断地址是否合法
2. 如果匹配不到，输入未匹配消息
3. 如果匹配到，依次输入匹配的内容

"""

import re
from dataclasses import dataclass

from tools.utils import address_util
from tools.utils.constant import (
    NO_ADDRESS_MATCHED_MSG,
    ADDRESS_MATCHED_MSG,
)
from tools.utils.pattern import ADDRESS_PATTERN


@dataclass(repr=False)
class AddressMatchedData(object):
    province: str
    city: str
    area: str
    street: str
    village: str
    number: str
    address: str
    room: str
    line: int = 1

    def __str__(self):
        address = "".join([self.province, self.city, self.area, self.street,
                           self.village, self.number, self.address, self.room])
        return ADDRESS_MATCHED_MSG.format(address=address, line=self.line)

    def is_valid(self) -> bool:
        """ 地址是否合法

        :return:
        """
        province = address_util.match_province(self.province)
        if not province:
            return False
        else:
            self.province = province

        return address_util.is_address_valid(self.province, self.city,
                                             self.area, self.street)


class AddressMatcher(object):
    def __init__(self):
        pass

    def process(self, data, line: int = 1):
        """ 正则匹配输入字符串，并打印匹配值

        :param data: 待匹配的字符串
        :param line: 行号
        """
        # 1. 根据规则对输入进行正则匹配
        matched = self.match(data, line)

        # 2. 如果匹配不到，输入未匹配消息
        # if not matched:
        #     print(NO_ADDRESS_MATCHED_MSG)

        # 3. 如果匹配到，依次输入匹配的内容
        for item in matched:
            print(item)

    @staticmethod
    def match(data: str, line: int = 1):
        """

        :param data: 待匹配字符串
        :param line: 行号
        :return:
        """
        result = []
        matched = re.findall(ADDRESS_PATTERN, data)
        for item in matched:
            address = AddressMatchedData(
                province=item[0],
                city=item[1],
                area=item[2],
                street=item[3],
                village=item[4],
                number=item[5],
                address=item[6],
                room=item[7],
                line=line
            )
            # 1.1 判断地址是否合法
            if address.is_valid():
                result.append(address)
        return result


if __name__ == '__main__':
    """ 在项目 `py_works` 根目录执行 `python -m tools.address` 测试 """

    cases = [
        "湖南省桃源县枫树维吾尔族回族乡牛场村03038号",
        "江西省南昌市青山湖区上海路382号12栋5单元601室",
        "福建省清流县余朋乡东坑村文化街61号",
        "上海市黄浦区复兴北路123号",
        "上海市番禺区复兴北路123号",
        "华容县",
        "测试上海市黄浦区复兴北路123号测试",
        "测试江西省青山湖区上海路382号12栋5单元601室测试",
    ]

    matcher = AddressMatcher()
    for index, case in enumerate(cases):
        print(f"address case: {index+1}")
        matcher.process(case)
        print("-" * 30)
