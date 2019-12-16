#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
以管道方式处理数据可
"""


class Task:
    def __init__(self):
        self.works = []
        
    def add_works(self, func):
        self.works.append(func)
        return self

    def process(self, path):
        with open(path) as f:
            for line_no, line in enumerate(f.readlines()):
                line = line.strip()
                if not len(line):
                    continue

                for func in self.works:
                    func(line, line=line_no+1)
