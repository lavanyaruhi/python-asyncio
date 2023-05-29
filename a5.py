import asyncio

async def task(name, delay):
    while True:
        print(f"Executing task {name}")
        await asyncio.sleep(delay)

async def main():
    # Create tasks
    task1 = asyncio.create_task(task("Task 1", 1))
    task2 = asyncio.create_task(task("Task 2", 2))
    task3 = asyncio.create_task(task("Task 3", 3))

    # Run the event loop
    await asyncio.gather(task1, task2, task3)

# Run the main program
asyncio.run(main())
