import asyncio 


_DEFAULT_HOST: str = "localhost"
_DEFAULT_PORT: int = 8000


async def handle_client(reader, writer):
    line = str()
    while line.strip() != 'quit':
        line = (await reader.readline()).decode('utf8').strip()
        if line == '': continue
        writer.write(line.encode())

    writer.close()


async def run_server():
    server = await asyncio.start_server(
        handle_client, _DEFAULT_HOST, _DEFAULT_PORT,
    )
    async with server:
        await server.serve_forever()


asyncio.run(run_server())
