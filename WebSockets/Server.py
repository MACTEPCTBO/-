import asyncio
import websockets


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

                print(data)
                await cls.Send(client,data)
        except Exception as e:
            await websocket.ping()
            print("Disconnect")
            await client.close()

    @classmethod
    async def Send(cls, client, data):
        await client.send(data)


async def main():
    async with websockets.serve(Connect.Connect,'127.0.0.1',3000):
        await asyncio.Future()


if __name__ == '__main__':
    asyncio.run(main())
