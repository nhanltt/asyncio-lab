# example of running a blocking io-bound task in asyncio 
import asyncio
import time 

# a blocking io-bound task 
def blocking_task():
    # report a message 
    print(f'{time.ctime()} Task starting... ')
    # block for a while 
    time.sleep(5)
    # report a message 
    print(f'{time.ctime()} Task done')

# main coroutine 
async def main():
    # report a message 
    print(f'{time.ctime()} Main running the blocking task')
    # create a coroutine for the blocking task 
    coro = asyncio.to_thread(blocking_task)
    # schedule the task 
    task = asyncio.create_task(coro)
    # report a message 
    print(f'{time.ctime()} Main doing other things')
    # allow the scheduled task to start 
    await asyncio.sleep(0)
    # await the task 
    await task

# run the asyncio program
asyncio.run(main())

# Running Result 
# Wed Jul 19 13:35:11 2023 Main running the blocking task
# Wed Jul 19 13:35:11 2023 Main doing other things
# Wed Jul 19 13:35:11 2023 Task starting...
# Wed Jul 19 13:35:16 2023 Task done