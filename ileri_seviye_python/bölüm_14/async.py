import asyncio
import time

async def fetch_data(id, delay):
    t = time.time()
    print(f"Fetching data for ID {id}...")
    await asyncio.sleep(delay)  # Simulate a long-running I/O operation
    print(f"Data fetched for ID {id}!")
    print(f"Elapsed time: {time.time() - t} seconds")
    return {"id": id, "data": "Sample data"}

#asyncio, Python'da asenkron programlama yapmak için kullanılan bir modüldür. 
# Asenkron programlama, bir işlemin tamamlanmasını beklemeden diğer işlemlere devam etmenizi sağlar. 
# Bu, özellikle I/O işlemleri gibi uzun süren işlemler için faydalıdır.
async def main(msg):
    t1 = time.time()
    print("starting")
    task = asyncio.create_task(fetch_data(2, 2))
    result = await task  # fetch_data fonksiyonunun tamamlanmasını bekliyoruz
    print("result:", result)
    #await ifadesi, bir asenkron fonksiyonun tamamlanmasını beklemek için kullanılır.
    await asyncio.sleep(2)
    print(msg)
    print(f"Total elapsed time: {time.time() - t1} seconds")
    
    task1 = asyncio.create_task(fetch_data(1, 3))
    task2 = asyncio.create_task(fetch_data(2, 2))
    results = await asyncio.gather(task1, task2)  # Birden fazla asenkron görevi aynı anda çalıştırmak için kullanılır.
    print("Results:", results)
#asyncio.run() fonksiyonu, bir asenkron fonksiyonu çalıştırmak için kullanılır.
asyncio.run(main("hello world"))
asyncio.run(main("hello world 2"))
