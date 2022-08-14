import threading
import asyncio
from datetime import datetime


def countdown_back_thread(number):
    from time import sleep

    for i in range(number, 0, -1):
        print(i)
        sleep(1)
        for k in range(10000000 * 3):
            pass


# def countdown(number):
#     t = threading.Thread(target=countdown_back_thread, args=(number,))
#     t.start()


start = datetime.now()
t1 = threading.Thread(target=countdown_back_thread, args=(5,))
t2 = threading.Thread(target=countdown_back_thread, args=(5,))
t3 = threading.Thread(target=countdown_back_thread, args=(5,))
t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
print(datetime.now() - start)


async def countdown_back_asyncio(number):
    for i in range(number, 0, -1):
        print(i)
        await asyncio.sleep(1)
        for k in range(10000000 * 3):
            pass


async def countdown_asyncio(number):
    t = asyncio.create_task(countdown_back_asyncio(number))
    await t


start = datetime.now()
loop = asyncio.get_event_loop()
tasks = asyncio.gather(countdown_asyncio(5), countdown_asyncio(5), countdown_asyncio(5))
loop.run_until_complete(tasks)
print(datetime.now() - start)

'''
asyncio помітно більш продуктивний у даному випадку
'''
