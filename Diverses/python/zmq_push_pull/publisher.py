""" Publisher """
import asyncio

import zmq.asyncio

context = zmq.asyncio.Context()
socket = context.socket(zmq.PUSH)


async def run():
    socket.bind('tcp://127.0.0.1:7000')
    print("Server is ready listening on port 7000")
    input("Press any key to start sending jobs!")
    await send()


async def send():
    print("About to send jobs!")
    for counter in range(20001):
        work_message = {'number': counter}
        await socket.send_json(work_message)

if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(run())

    except KeyboardInterrupt:
        exit()
