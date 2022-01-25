from argparse import ArgumentParser
import asyncio
import time
import zmq.asyncio
import zmq

context = zmq.asyncio.Context()
socket = context.socket(zmq.PAIR)


async def run(port):
    socket.connect(f'tcp://127.0.0.1:{port}')
    print(f"Server is ready listening on port {port}")

    round = 1
    while True:
        message = await socket.recv_string()
        print(message)
        await socket.send_string(f"Send Client message nr. {round} to Server1")
        round += 1
        await socket.send_string(f"Send Client message nr. {round} to Server2")
        round += 1

        time.sleep(1)

if __name__ == '__main__':
    try:
        parser = ArgumentParser()
        parser.add_argument("-p", "--port", type=str, default="5556")
        port = parser.parse_args().port
        loop = asyncio.get_event_loop()
        loop.run_until_complete(run(port))

    except KeyboardInterrupt:
        exit()
