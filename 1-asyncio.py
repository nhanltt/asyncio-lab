# example of running a coroutine
import asyncio

# define a coroutine
async def custom_coro():
    # wait for a task to be done 
    # await another coroutine 
    await asyncio.sleep(1)

# main coroutine 
async def main():
    # execute custom coroutine
    await custom_coro()

# start the coroutine program
asyncio.run(main())