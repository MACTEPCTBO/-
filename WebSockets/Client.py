import asyncio
import threading
from threading import Thread

import websockets


class Client:
    @classmethod
    async def Connect(cls,i):
        try:
            async with websockets.connect('ws://127.0.0.1:3000') as client:
                while True:
                    #data = input('Введите данные для отправки + \n')
                    data = '123'
                    await client.send(data)

                    print(await client.recv())
        except:
            print(i)
            await asyncio.sleep(1_000_000)

                #await asyncio.sleep(100000)

    @classmethod
    async def Test(cls):
        for j in range(100):
            target = []
            loop = asyncio.get_event_loop()
            for i in range(1_000):
                t = loop.create_task(Client.Connect(i))
                target.append(t)

            #print('123456')
            await asyncio.wait(target)



if __name__ == '__main__':
    asyncio.run(Client.Connect(0))
