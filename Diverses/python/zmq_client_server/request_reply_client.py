from argparse import ArgumentParser
import asyncio
import zmq.asyncio
import zmq

context = zmq.asyncio.Context()
socket = context.socket(zmq.REQ)


async def run(ports):
    print(f"Connecting to Servers:")
    for port in ports:
        con_str = f'tcp://127.0.0.1:{port}'
        socket.connect(con_str)
        print(con_str)
    await send()


async def send():
    for request in range(1, 10):
        print("Sending request ", request, "...")
        await socket.send_json({"data": {'request_number': request}})
        await get_reply(request)


async def get_reply(request):
    message = await socket.recv_json()
    print(f"Received reply: {request} with Data: {message}")


if __name__ == '__main__':
    try:
        parser = ArgumentParser()
        parser.add_argument("-p", "--ports", nargs="+", default=["5556"])
        ports = parser.parse_args().ports
        loop = asyncio.get_event_loop()
        loop.run_until_complete(run(ports))

    except KeyboardInterrupt:
        exit()
