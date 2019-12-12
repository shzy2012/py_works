#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
以管道方式处理数据可
"""

from itertools import islice

class Task:
    def __init__(self):
        self.works=[]
        
    def AddWorks(self,func):
        self.works.append(func)
        return self

    def Do(self,path):
        with open(path) as f:
            while True:
                next_n_lines = list(islice(f, 100))
                if not next_n_lines:
                    return next_n_lines
                # process next_n_lines
                result = next_n_lines
                for func in self.works:
                    result = func(next_n_lines)
                print(result)