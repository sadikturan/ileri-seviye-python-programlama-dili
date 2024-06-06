import asyncio
import time

async def fetch_data(id, delay):
    print("veri alınıyor...id:", id)
    await asyncio.sleep(delay)
    print("veri alındı... id:", id)
    return {"id": id, "data": "bazı veriler"}

async def main():
    tasks = []

    for id, delay in enumerate([2,1,3], start=1):
        tasks.append(asyncio.create_task(fetch_data(id, delay)))
    
    await asyncio.gather(*tasks)
    
t = time.time()
asyncio.run(main())
print(time.time() - t)