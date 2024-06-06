import asyncio
import time

async def fetch_data(id, delay):
    print("veri alınıyor...id:", id)
    await asyncio.sleep(delay)
    print("veri alındı... id:", id)
    return {"id": id, "data": "bazı veriler"}

async def main():
    task1 = asyncio.create_task(fetch_data(1, 2))
    task2 = asyncio.create_task(fetch_data(2, 3))
    task3 = asyncio.create_task(fetch_data(3, 1))

    result1 = await task1
    print(f"alınan veri: {result1}")

    result2 = await task2
    print(f"alınan veri: {result2}")

    result3 = await task3
    print(f"alınan veri: {result3}")
    
t = time.time()
asyncio.run(main())
print(time.time() - t)