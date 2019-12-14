#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from tools.task import Task
from tools.address import Address
from tools.phone import PhoneMatcher
from tools.ID import ID

# 
address = Address()
phone = PhoneMatcher()
id = ID()

# 运算
path = os.getcwd() + '/data/data1.txt'
task = Task()
task.AddWorks(address.Do).AddWorks(phone.process).AddWorks(id.Do).process(path)
