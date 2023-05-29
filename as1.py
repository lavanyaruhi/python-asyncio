import asyncio

async def handle_client(reader, writer):
    while True:
        data = await reader.read(100)
        message = data.decode().strip()
        print(f"Received message from client: {message}")
        #response = "Hello from the server!"
        if message == 'exit':
            writer.write('goodbye'.encode())
            await writer.drain()
            writer.close()
        response = f'you said:{message}\n'
        writer.write(response.encode())
        await writer.drain()
        #writer.close()

async def main():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8888)
    addr = server.sockets[0].getsockname()
    print(f'Server started on {addr}')

    async with server:
        await server.serve_forever()

asyncio.run(main())
