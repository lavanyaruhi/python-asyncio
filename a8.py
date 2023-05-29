import asyncio

async def read_file():
    with open("data.txt", "r") as file:
        data = file.read()
        print("Read data:", data)

async def write_file():
    with open("data.txt", "w") as file:
        file.write("Hello, world!")
        print("Data written")

async def main():
    await asyncio.gather(read_file(), write_file())

asyncio.run(main())
