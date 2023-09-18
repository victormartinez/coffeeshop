import asyncio

import settings
from coffeeshop.app.factory import create_ai_service


async def handle_client(
    reader: asyncio.StreamReader, writer: asyncio.StreamWriter
) -> None:
    line = str()
    ai_service = await create_ai_service()
    while line.strip() != "quit":
        line = (await reader.readline()).decode("utf8").strip()
        if line == "":
            continue
        print(f"Guest: {line}")
        answer: str = await ai_service.reply(line)
        print(f"Employee: {answer}")
        writer.write(line.encode())

    writer.close()


async def run_server() -> None:
    server = await asyncio.start_server(
        handle_client,
        settings.DEFAULT_HOST,
        settings.DEFAULT_PORT,
    )
    async with server:
        await server.serve_forever()


asyncio.run(run_server())
