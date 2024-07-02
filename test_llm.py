from metagpt.llm import LLM
import asyncio
llm = LLM()
asyncio.run(llm.aask("你是什么模型"))