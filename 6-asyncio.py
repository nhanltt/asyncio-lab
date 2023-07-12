# example of waiting for a coroutine with a timeout 
from random import random
import asyncio
import time

# coroutine to execute in a new task 
async def task_coro(arg):
    # generate a random value between 0 and 1 
    value = 1 + random()
    # report message 
    print(f'{time.ctime()} > task got {value}')
    # block for a moment
    await asyncio.sleep(value)
    # report all done 
    print(f'{time.ctime()} > task done')

# main coroutine
async def main():
    # create a task 
    task = task_coro(1)
    # execute and wait for the task witphout a timeout 
    try:
        await asyncio.wait_for(task, timeout=0.5)
    except asyncio.TimeoutError:
        print(f'{time.ctime()} Gave up waiting, task cancelled')

# start the asyncio program 
asyncio.run(main())