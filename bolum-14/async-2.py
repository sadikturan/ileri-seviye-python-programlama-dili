import asyncio

async def fetch_data(delay):
    print("veri alınıyor...")
    await asyncio.sleep(delay)
    print("veri alındı...")
    return {"data": "bazı veriler"}

async def main():
    print("start")
    task = fetch_data(2)
    print("end")

    result = await task
    print(f"alınan veri: {result}")
    

asyncio.run(main())