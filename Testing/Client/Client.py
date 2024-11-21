import asyncio
import json

import websockets
import threading


class Client:
    data = []
    def __init__(self, Ip: str, Port: int):
        self.IP = Ip
        self.Port = Port

        self.data = '1'


    async def Connect(self):
        async with websockets.connect(f'ws://{self.IP}:{self.Port}') as self.client:
            await self.Send(('42215'))
            await self.Recv()

            await self.client.close()




    async def Send(self, data: tuple):
        data = json.dumps(data)
        print(data)
        await self.client.send(data)


    async def Recv(self) -> list:
        data = await self.client.recv()
        data = json.loads(data)
        print("RECV " + str(data))

        self.data = data


if __name__ == '__main__':
    c = Client('127.0.0.1',3000)
    asyncio.run(c.Connect())