import sys

import asyncio

import settings
from coffeeshop import utils


async def run_client(filepath: str) -> None:
    try:
        sentences = await utils.input_to_sentences(filepath)
        reader, writer = await asyncio.open_connection(settings.DEFAULT_HOST, settings.DEFAULT_PORT)
        for row in sentences:
            if not row:
                break

            writer.write(f"{row}\n".encode())
            data = await reader.read(100000)
            print(data.decode().strip())

    except OSError as exc:
        print(str(exc))

asyncio.run(run_client(filepath=sys.argv[1]))
