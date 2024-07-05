# main.py
import asyncio
from metagpt.roles.di.data_interpreter import DataInterpreter
from metagpt.tools.libs import calculator

async def main(requirement: str):
   role = DataInterpreter(tools=["calculator"])   # 集成工具
   await role.run(requirement)

if __name__ == "__main__":
   requirement = "请计算 3 和 11 的和，然后计算 5 的阶乘"
   asyncio.run(main(requirement))