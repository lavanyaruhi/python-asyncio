import asyncio

async def my_coroutine(writer):
    data = b"Hello, World!"

    writer.write(data)
    # No await writer.drain() here

    writer.close()

async def main():
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

    await my_coroutine(writer)


asyncio.run(main())
