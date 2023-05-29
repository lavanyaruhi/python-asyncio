import asyncio
async def handle(reader,writer):
    while True:
        data = await reader.read(102)
        message = data.decode().strip()
        print(f"Received message from client: {message}")
        if message == 'exit':
            writer.write('goodbye'.encode())
            await writer.drain()
            writer.close()
          #  return
        
        response = f'you said:{message}\n'
        writer.write(response.encode())
        await writer.drain()
        
async def main():
    server = await asyncio.start_server(handle,'127.0.0.1',8888)
    addr = server.sockets[0].getsockname()
    print(f'Server started on {addr}')
    try:
        await server.serve_forever()
    finally:
        server.close()
        await server.wait_closed()
    #async with server:
     #   await server.serve_forever()

asyncio.run(main())