import asyncio 

import settings
from coffeeshop.employee.service import process


async def handle_client(reader, writer):
    line = str()
    while line.strip() != 'quit':
        line = (await reader.readline()).decode('utf8').strip()
        if line == '': continue

        print(f'Guest: {line}')
        answer: str = await process(line)
        print(f'Employee: {answer}')

        writer.write(answer.encode())

    writer.close()
    print('Come back anytime.')


async def run_server():
    server = await asyncio.start_server(
        handle_client, settings.DEFAULT_HOST, settings.DEFAULT_PORT
    )
    async with server:
        print('Employer: Welcome to our coffee shop. What can I get you?')
        await server.serve_forever()


asyncio.run(run_server())
