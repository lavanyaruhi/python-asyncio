import asyncio
async def client_message():
    reader,writer = await asyncio.open_connection('127.0.0.1',8888)
    while True:
        message = input("enter:")
        writer.write(message.encode())
        await writer.drain()
        if message == 'exit':
            response = await reader.read(100)
            print(response.decode())
            writer.close()
            #return
        response = await reader.read(100)
        print(response.decode())
asyncio.run(client_message())
 