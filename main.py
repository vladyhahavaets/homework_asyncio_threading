import threading


# функція для відрахунку
def countdown_back_thread(number):
    from time import sleep

    for i in range(number, 0, -1):
        print(i)
        sleep(1)


# функція для запуску окремого потоку
def countdown(number):
    t = threading.Thread(target=countdown_back_thread, args=(number,))
    t.start()


# countdown(4)
# countdown(4)
# countdown(4)

import asyncio




async def countdown_back_asyncio(number):

    for i in range(number, 0, -1):
        print(i)
        await asyncio.sleep(1)


async def countdown_asyncio(number):
    t = asyncio.create_task(countdown_back_asyncio(number))
    await t

loop = asyncio.get_event_loop()
tasks = asyncio.gather(countdown_asyncio(5),countdown_asyncio(5),countdown_asyncio(5) )
loop.run_until_complete(tasks)
