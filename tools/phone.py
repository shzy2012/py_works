#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
号码匹配:
1. 根据规则对输入进行正则匹配
2. 如果匹配不到，输入未匹配消息
3. 如果匹配到，依次输入匹配的内容

"""

import re
from dataclasses import dataclass

from tools.utils.constant import (
    DEFAULT_PHONE_TYPE,
    MOBILE_PHONE,
    FIXED_TELEPHONE,
    PHONE_TYPE_UNSUPPORTED_MSG,
    DEFAULT_PHONE_MATCHED_MSG,
    MOBILE_PHONE_MATCHED_MSG,
    FIXED_TELEPHONE_MATCHED_MSG,
    NO_PHONE_MATCHED_MSG,
)
from tools.utils.pattern import (
    MOBIL_PHONE_PATTERN,
    FIXED_TELEPHONE_PATTERN,
)


@dataclass(repr=False)
class PhoneMatchedData(object):
    phone_num: str
    phone_type: str
    line: int = 1

    def __str__(self):
        if self.phone_type == MOBILE_PHONE:
            return MOBILE_PHONE_MATCHED_MSG.format(phone=self.phone_num,
                                                   line=self.line)
        elif self.phone_type == FIXED_TELEPHONE:
            return FIXED_TELEPHONE_MATCHED_MSG.format(phone=self.phone_num,
                                                      line=self.line)
        else:
            return DEFAULT_PHONE_MATCHED_MSG.format(phone=self.phone_num,
                                                    line=self.line)


class PhoneMatcher(object):

    def __init__(self):
        # self.matched: List[PhoneMatchedData] = []
        pass

    def process(
            self,
            data,
            phone_type: str = DEFAULT_PHONE_TYPE,
            line: int = 1
    ):
        """ 正则匹配输入字符串，并打印匹配值

        :param data: 待匹配的字符串
        :param phone_type: 需要匹配的号码类型，默认国内手机号
        :param line: 行号
        """
        # 1. 根据规则对输入进行正则匹配
        matched = self.match(data, phone_type, line)

        # 2. 如果匹配不到，输入未匹配消息
        # if not matched:
        #     print(NO_PHONE_MATCHED_MSG)

        # 3. 如果匹配到，依次输入匹配的内容
        for item in matched:
            print(item)

    def match(
            self,
            data: str,
            phone_type: str = DEFAULT_PHONE_TYPE,
            line: int = 1
    ):
        """ 正则匹配输入字符串 
        
        :param data: 待匹配的字符串
        :param phone_type: 需要匹配的号码类型，默认国内手机号
        :param line: 行号
        """
        if phone_type == MOBILE_PHONE:
            return self._match_mobile_phone(data, line)
        elif phone_type == FIXED_TELEPHONE:
            return self._match_fix_telephone(data, line)
        else:
            print(PHONE_TYPE_UNSUPPORTED_MSG.format(phone_type=phone_type))
            return []

    @staticmethod
    def _match_mobile_phone(data: str, line: int = 1):
        """ 正则匹配国内手机号

        :param data: 待匹配的字符串
        :param line: 行号
        """
        matched = re.findall(MOBIL_PHONE_PATTERN, data)
        result = []
        for item in matched:
            result.append(PhoneMatchedData(
                phone_num=item,
                phone_type=MOBILE_PHONE,
                line=line
            ))
        return result

    @staticmethod
    def _match_fix_telephone(data: str, line: int = 1):
        """ 正则匹配国内固定电话

        :param data: 待匹配的字符串
        :param line: 行号
        """
        matched = re.findall(FIXED_TELEPHONE_PATTERN, data)
        result = []
        for item in matched:
            result.append(PhoneMatchedData(
                phone_num=item[0],
                phone_type=FIXED_TELEPHONE,
                line=line
            ))
        return result


if __name__ == "__main__":

    """ 在项目 `py_works` 根目录执行 `python -m tools.phone` 测试 """
    mobile_phone_cases = [
        "hahah 11115021801933hahahhahhahah18919231909111",
        "150218019331234567890",
        "hahah15021801933hahahhahhahah 18919231909",
        "(+86) 15021801933 haha",
        "(+86）15021801933haha",
        "+86 15021801933haha",
    ]

    fixed_telephone_cases = [
        "haha 11021-8879203haha0102201220211",
        "11021-887920311",
        "haha 021-88792031haha01022012202",
        "(+86) 021-88792031 haha",
        "(+86）021-88792031",
        "+86 021-88792031",
    ]

    for index, case in enumerate(mobile_phone_cases):
        phone_matcher = PhoneMatcher()
        print(f"mobile_phone case: {index+1}")
        phone_matcher.process(case)
        print("-" * 30)

    for index, case in enumerate(fixed_telephone_cases):
        phone_matcher = PhoneMatcher()
        print(f"fixed_telephone case: {index+1}")
        phone_matcher.process(case, phone_type=FIXED_TELEPHONE)
        print("-" * 30)
