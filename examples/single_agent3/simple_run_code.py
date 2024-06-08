import subprocess
from metagpt.actions.action import Action
from metagpt.logs import logger

class SimpleRunCode(Action):
    name: str = "SimpleRunCode"

    async def run(self, code_text: str):
        # logger.info(f"{code_text=}")
        result = subprocess.run(["python", "-c", code_text], capture_output=True, text=True)
        code_result = result.stdout
        logger.info(f"{code_result=}")
        return code_result