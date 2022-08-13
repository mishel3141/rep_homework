#  Создать функцию, которая принимает число и начинает обратный отсчет с интервалом
#  в 1 секунду. Запустить 5 таких функции параллельно. Сделать 2 варианта через
#  threading, и через asyncio. По наблюдениям описать что работает лучше и почему
#  (необязательно). Запушить в гит и скинуть ссылку.
#

import threading
from time import sleep
import time

def countdown(n):
    print(f'начат отсчет {n}')
    i = n
    while i >= 0:
        i -= 1
        sleep(1)
    print(f'закончен отсчет {n}')

print('_________ Синхронный режим ___________')

start = time.time()
countdown(15)
countdown(11)
countdown(7)
countdown(5)
countdown(13)

print('синхронный процесс завершен за ' + str(round(time.time()-start, 3)) + ' сек')

print('_________ Асинхронность с threading ___________')

task1 = threading.Thread(target=countdown, args=(15,))
task2 = threading.Thread(target=countdown, args=(11,))
task3 = threading.Thread(target=countdown, args=(7,))
task4 = threading.Thread(target=countdown, args=(5,))
task5 = threading.Thread(target=countdown, args=(13,))
start = time.time()
task1.start()
task2.start()
task3.start()
task4.start()
task5.start()
task1.join()

print('процесс с threading завершен за ' + str(round(time.time()-start, 3)) + ' сек')

import asyncio
import time

async def countdown(n):
    print(f'начат отсчет {n}')
    i = n
    while i >= 0:
        i -= 1
        await asyncio.sleep(1)
    print(f'закончен отсчет {n}')

print('_________ Асинхронность с asyncio ___________')

async def count():
    t1 = asyncio.create_task(countdown(15))
    t2 = asyncio.create_task(countdown(11))
    t3 = asyncio.create_task(countdown(7))
    t4 = asyncio.create_task(countdown(5))
    t5 = asyncio.create_task(countdown(13))
    await t1
    await t2
    await t3
    await t4
    await t5

start = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(count())
loop.close()
task1.join()                  # вставлено для чистоты эксперимента

print('процесс с asyncio завершен за ' + str(round(time.time()-start, 3)) + 'сек')
