""" Result Collector """
import asyncio
import zmq.asyncio
import time


context = zmq.asyncio.Context()
result_collector_receiver = context.socket(zmq.PULL)


async def run():
    result_collector_receiver.bind('tcp://127.0.0.1:7001')

    print("Result Collector Connected to Server")
    start_time = time.time()
    zmq_data = {}
    while True:
        zmq_message = await result_collector_receiver.recv_json()
        if "worker" in zmq_message:
            worker = zmq_message.get('worker')
            if worker in zmq_data:
                zmq_data[worker] += 1
            else:
                zmq_data[worker] = 1
        if zmq_message.get('finished'):
            print(zmq_data)
            zmq_data = {}


if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(run())
    except KeyboardInterrupt:
        exit()
