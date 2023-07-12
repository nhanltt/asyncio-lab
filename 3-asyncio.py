# example of starting many tasks and getting access to all tasks
import asyncio
import time 

# coroutine for a taks
async def task_coroutine(value):
    # report message
    print(f'{time.ctime()} task {value} is running')
    # block for a moment
    await asyncio.sleep(0.2)

# define a main coroutine 
async def main():
    # report message
    print(f'{time.ctime()} main coroutine started')
    # start many task 
    started_tasks = [asyncio.create_task(task_coroutine(i)) for i in range(10)]
    # allow some of the tasks time to start 
    await asyncio.sleep(0.1)
    # get all tasks 
    tasks = asyncio.all_tasks()
    # report all tasks
    for task in tasks:
        print(f'{time.ctime()} > {task.get_name()}, {task.get_coro()}')

    for task in started_tasks:
        await task


asyncio.run(main())