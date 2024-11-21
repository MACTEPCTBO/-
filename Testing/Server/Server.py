import asyncio
import json
import websockets


from Connector import Connector
from websockets import ConnectionClosedError, ConnectionClosed


class Connect:

    @classmethod
    async def Connect(cls, client):
        await cls.Recv(client)



    @classmethod
    async def Recv(cls, client):
        print(f'Connect: user')
        try:
            while True:
                data = await client.recv()
                data = json.loads(data)

                if data:
                    data = await Connector.OpenFile(data)
                await cls.Send(client,data)


        except ConnectionClosedError as e:
            print("Error: " + str(e))
            await client.close()
        except ConnectionClosed as e:
            print("Disconnect: ")
            await client.close()

    @classmethod
    async def Send(cls, client, data):
        data = json.dumps(data)
        await client.send(data)


async def main():
    async with websockets.serve(Connect.Connect,'127.0.0.1',3000):
        await asyncio.Future()


if __name__ == '__main__':
    asyncio.run(main())