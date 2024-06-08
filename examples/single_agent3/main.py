import asyncio

from runnable_coder import RunnableCoder
from metagpt.context import Context
from metagpt.logs import logger

async def main():
    msg = "write a function that calculates the sum of a list"
    context = Context()
    role = RunnableCoder(context=context)
    logger.info(msg)
    result = await role.run(msg)
    logger.info(result)

if __name__ == '__main__':
    asyncio.run(main())