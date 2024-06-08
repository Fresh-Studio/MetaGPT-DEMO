import asyncio

from simple_coder import SimpleCoder
from metagpt.logs import logger
from metagpt.context import Context

async def main():
    msg = "write a function that calculates the sum of a list"
    context = Context()
    role = SimpleCoder(context=context)
    logger.info(msg)
    result = await role.run(msg)
    logger.info(result)

if __name__ == '__main__':
    asyncio.run(main())