import time
import logging
import asyncio


logging.basicConfig(filename='myapp.log', level=logging.INFO,)

logger = logging.getLogger(__name__)



async def mock_api_rquest(i):
        logger.info(f"Request of API START > {i}")
        await asyncio.sleep(1)
        logger.info(f"Reques of API END < {i}")


async def start():
    for i in range(1000_000):
        await mock_api_rquest(i)

asyncio.run(start())
