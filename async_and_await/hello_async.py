import asyncio
import time


def sync_hello():
    print('hello')
    time.sleep(3)
    print('world')


async def async_hello():
    print('hello')
    await asyncio.sleep(3)
    print('world')


async def main():
    # sync_hello()
    task1 = asyncio.create_task(async_hello())
    task2 = asyncio.create_task(async_hello())
    await asyncio.gather(
        task1,
        task2
    )

if __name__ == '__main__':
    asyncio.run(main())
