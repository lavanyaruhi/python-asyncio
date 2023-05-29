import asyncio

async def hello_world():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

async def main():
    await hello_world()

asyncio.run(main())
