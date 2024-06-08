import asyncio
from asyncio.log import logger

from metagpt.context import Context

from examples.single_agent2.simple_coder import SimpleCoder

async def main():
    msg = "write a function that calculates the sum of a list"
    context = Context()
    role = SimpleCoder(context=context)
    logger.info(msg)
    result = await role.run(msg)
    logger.info(result)

asyncio.run(main)