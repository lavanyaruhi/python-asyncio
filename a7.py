import asyncio

async def my_coroutine():
    print("Coroutine started")
    await asyncio.sleep(2)
    print("Coroutine completed")

async def main():
    try:
        await asyncio.wait_for(my_coroutine(), timeout=1)
    except asyncio.TimeoutError:
        print("Coroutine took too long")

asyncio.run(main())
