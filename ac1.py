import asyncio

async def send_message():
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
    message = "Hello from the client!"
    writer.write(message.encode())
    await writer.drain()
    data = await reader.read(100)
    response = data.decode()
    print(f"Received response from server: {response}")
    writer.close()

asyncio.run(send_message())
