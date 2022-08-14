import threading
import asyncio


def countdown_back_thread(number):
    from time import sleep

    for i in range(number, 0, -1):
        print(i)
        sleep(1)


def countdown(number):
    t = threading.Thread(target=countdown_back_thread, args=(number,))
    t.start()


countdown(5)
countdown(5)
countdown(5)


async def countdown_back_asyncio(number):
    for i in range(number, 0, -1):
        print(i)
        await asyncio.sleep(1)


async def countdown_asyncio(number):
    t = asyncio.create_task(countdown_back_asyncio(number))
    await t


loop = asyncio.get_event_loop()
tasks = asyncio.gather(countdown_asyncio(5), countdown_asyncio(5), countdown_asyncio(5))
loop.run_until_complete(tasks)

'''
при тестуванні продуктивності (попередній комміт (посилання знизу)), можна помітити, що asyncio кращий у даному випадку
у цій задачі нам не потрібно розпаралелювати розрахунки, тому нам потрібна НЕ багатопоточність.
у даному випадку є затримка, під час якої програма нічого не робить (інтервал в одну секунду і є затримкою), тому краще 
використовувати асинхронність.
'''
'https://github.com/vladyhahavaets/homework_asyncio_threading/commit/166d63a6b51f67c542538943395a6e54f7f561a4'
