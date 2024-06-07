# 可导入任何角色，初始化它，用一个开始的消息运行它，完成！
import asyncio

from metagpt.context import Context
from metagpt.roles.product_manager import ProductManager
from metagpt.logs import logger

async def main():
    name = "Bomb Yang"
    profile = "buyer"
    msg = "Write a PRD for a snake game"
    context = Context()  # 显式创建会话Context对象，Role对象会隐式的自动将它共享给自己的Action对象
    role = ProductManager(name=name, profile=profile, context=context)
    while msg:
        msg = await role.run(msg)
        logger.info(str(msg))

if __name__ == '__main__':
    asyncio.run(main())