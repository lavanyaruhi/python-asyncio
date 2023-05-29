import asyncio

async def coroutine_1():
    print("Coroutine 1 started")
    await asyncio.sleep(1)
    print("Coroutine 1 completed")

async def coroutine_2():
    print("Coroutine 2 started")
    await asyncio.sleep(2)
    print("Coroutine 2 completed")

async def main():
    await asyncio.gather(coroutine_1(), coroutine_2())

asyncio.run(main())
