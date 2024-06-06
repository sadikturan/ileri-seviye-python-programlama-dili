import asyncio

async def main(msg):
    print("start")
    await asyncio.sleep(2)
    print(msg)

asyncio.run(main("merhaba"))