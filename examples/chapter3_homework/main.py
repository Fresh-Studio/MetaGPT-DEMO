#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2024/7/14 21:13
@Author  : yusingh
@File    : main.py
Homework of Chapter 3(https://www.feishu.cn/community/article/wiki?id=7382188504203132929)
"""
from metagpt.actions import Action
from metagpt.roles import Role

class Print(Action):
    """Action class for printing some informations

    Args:
        name: name of action
        info: info to print
    """

    name: str = "Print"
    info: str = ""

    async def run(self):
        print("打印{info}")

class Printer(Role):
    """Role of printer
    """

    name: str = "Printer"

    def __init__(self, **kwargs):
        super.__init__(kwargs)
        self.set_actions([Print(info="1"), Print(info="2"), Print(info="3")])

    def 