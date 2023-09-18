import asyncio
import sys

import settings
from coffeeshop.infrastructure.file.reader import read_file


async def run_client(filepath: str) -> None:
    try:
        reader, writer = await asyncio.open_connection(
            settings.DEFAULT_HOST, settings.DEFAULT_PORT
        )
        async for sentence in read_file(filepath):
            if sentence:
                writer.write(f"{sentence}\n".encode())
                data = await reader.read(100000)
                print(data.decode().strip())

        writer.close()
        await writer.wait_closed()
    except OSError as exc:
        print(str(exc))


asyncio.run(run_client(filepath=sys.argv[1]))
