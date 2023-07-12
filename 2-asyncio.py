# example of getting the current task from the main coroutine
import asyncio
import time
# define a coroutine

# define a main coroutine
async def main():
    # report a message
    print(f'{time.ctime()} main coroutin started!')
    
    # get the current task 
    task = asyncio.current_task()
    # report its details
    print(f'{time.ctime()} ',task)

# start the asyncio program
asyncio.run(main())