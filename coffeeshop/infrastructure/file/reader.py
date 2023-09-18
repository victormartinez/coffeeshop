import aiofiles


async def read_file(filepath: str) :
    async with aiofiles.open(filepath, mode='r') as f:
        yield await f.readline()
