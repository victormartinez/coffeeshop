from typing import AsyncGenerator

import aiofiles  # type: ignore[import]


async def read_file(filepath: str) -> AsyncGenerator[str, str]:
    async with aiofiles.open(filepath, mode="r") as f:
        async for line in f:
            yield line
