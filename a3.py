import asyncio
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    url = "https://www.example.com"
    response = await fetch(url)
    print(f"Response from {url}: {response[:1000]}")

asyncio.run(main())
