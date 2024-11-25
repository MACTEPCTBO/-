import asyncio
import logging
import random
import websockets


class Client:
    client = None

    @classmethod
    async def Connect(cls,i):
        try:
            await asyncio.sleep(random.randint(0,15))
            async with websockets.connect('ws://127.0.0.1:3000',logger=logging.getLogger("websockets.client")) as cls.client:
                asyncio.create_task(cls.AutoSend())
                while True:
                    await asyncio.sleep(25)

                    data = '123'
                    await cls.client.send(data)

                    await cls.client.recv()
                    #print(await cls.client.recv())
        except websockets.ConnectionClosed:
            print('reconnect')

            #await asyncio.sleep(1_000_000)
            await cls.Connect(i)


    @classmethod
    async def Test(cls):
        #for j in range(100):
            target = []
            loop = asyncio.get_event_loop()
            for i in range(2):
                t = loop.create_task(Client.Connect(i))
                target.append(t)

            #print('123456')
            await asyncio.wait(target)


    @classmethod
    async def AutoSend(cls):
        while True:
            await cls.client.send('send')
            await asyncio.sleep(15)
            #print('Авто-отправка')


if __name__ == '__main__':
    asyncio.run(Client.Test())
