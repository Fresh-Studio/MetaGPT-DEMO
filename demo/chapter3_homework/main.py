#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2024/7/14 21:13
@Author  : yusingh
@File    : main.py
Homework of Chapter 3(https://www.feishu.cn/community/article/wiki?id=7382188504203132929)
"""
from metagpt.actions import Action
from metagpt.roles.role import Role, RoleReactMode
from metagpt.schema import Message
from metagpt.logs import logger

import asyncio
import time

class Print(Action):
    """
    Action class for printing some informations

    Args:
        name: name of action
        info: info to print
    """

    name: str = "Print"
    info: int = 0

    async def run(self) -> Message:
        print(f"print {self.info}")
        return Message(content=f"print {self.info} success")

class Printer(Role):
    """
    Role of printer
    """

    name: str = "Printer"
    profile: str = "Print some informations"
    current: int = 1

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        actions = []
        batch = 3
        while batch > 0:
            actions.append(Print(info = self.current))
            self.current += 1
            batch -= 1

        self.set_actions(actions)
        self._set_react_mode(react_mode=RoleReactMode.REACT.value)

    async def _react(self) -> Message | None:
        """
        perform loop of think->act->think->act

        Returns:
            A message containing the final result of Printer.
        """
        msg = None
        while True:
            await self._think()
            if self.rc.todo is None:
                actions = []
                batch = 3
                while batch > 0:
                    batch -= 1
                    actions.append(Print(info = self.current))
                    self.current += 1
                    
                self.set_actions(actions)
                self._set_state(0)

                time.sleep(1)

            msg = await self._act()
        
        return msg
    
    async def _think(self) -> None:
        """
        decide which action should be done next time
        """
        logger.info(self.rc.state)
        if self.rc.todo is None:
            self._set_state(0)
            return
        
        if self.rc.state + 1 < len(self.states):
            self._set_state(self.rc.state + 1)
        else:
            self.rc.todo = None

    async def _act(self) -> Message:
        """
        perform the action determined by _think

        Returns:
            A message containing the result of the action.
        """
        todo = self.rc.todo
        return await todo.run()
    
async def main():
    role = Printer()

    logger.info(role)

    result = await role.run("start to print")

    logger.info(result)

asyncio.run(main())