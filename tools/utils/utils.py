# -*- coding: utf-8 -*-

# @Time       : 2019/12/15 14:47
# @Author     : fanchunke
# @Email      : fanchunke@laiye.com
# @FileName   : utils.py
# @Description:

"""
判断地址是否合法
0. 载入行政区划数据
1. 判断省级是否有效。无效直接返回，有效继续后面的判断
2. 判断地级是否有效
    2.1 如果地级输入存在，判断地级是否有效。无效直接返回，有效继续后面的判断
    2.2 如果地级输入不存在，则继续后面的判断
3. 判断县级是否有效。无效直接返回，有效继续后面的判断
4. 判断乡级是否有效。无效直接返回，有效返回地址合法
"""

import json


class AddressUtil(object):

    def __init__(self):
        self.pcas = dict()
        self._init()

    def _init(self):
        # 0. 载入行政区划数据
        with open('data/pcas.json', encoding='utf-8') as f:
            self.pcas = json.load(f)

    def match_province(self, data: str):
        """ 从待匹配字符串中匹配省份

        :param data: 待匹配字符串
        :return:
        """
        province_names = self.pcas.keys()
        for name in province_names:
            if name in data:
                return name
        return None

    def is_address_valid(self, province, city, area, street):
        """ 地址是否有效

        :param province: 省级（省份、直辖市、自治区）
        :param city: 地级（城市）
        :param area: 县级（区县）
        :param street: 乡级（乡镇、街道）
        :return:
        """
        # 1. 判断省级是否有效。无效直接返回，有效继续后面的判断
        province_data = self.pcas.get(province)
        if not province_data:
            return False

        # 2. 判断地级是否有效
        assert isinstance(province_data, dict)
        # 2.1 如果地级输入存在，判断地级是否有效。无效直接返回，有效继续后面的判断
        if city:
            city_data = province_data.get(city)
            if not city_data:
                return False
        # 2.2 如果地级输入不存在，则继续后面的判断
        else:
            city_data = {}
            for item in province_data.values():
                assert isinstance(item, dict)
                city_data.update(item)

        # 3. 判断县级是否有效。无效直接返回，有效继续后面的判断
        area_data = city_data.get(area)
        if not area_data:
            return False

        # 4. 判断乡级是否有效。无效直接返回，有效返回地址合法
        if street and street not in area_data:
            return False

        return True


address_util = AddressUtil()
