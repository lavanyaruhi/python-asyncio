import asyncio

# Define a generator-based coroutine
async def count_up_to(n):
    for i in range(1, n + 1):
        yield i
        await asyncio.sleep(1)  # Simulate an asynchronous operation

# Define an asyncio event loop
loop = asyncio.get_event_loop()

# Create a coroutine object
coroutine = count_up_to(5)

# Run the coroutine using the event loop
try:
    loop.run_until_complete(coroutine)
finally:
    loop.close()
