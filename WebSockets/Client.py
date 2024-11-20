import asyncio
import websockets


class Client:
    @classmethod
    async def Connect(cls):
        print("Connect server")
        async with websockets.connect('ws://127.0.0.1:3000') as client:
            while True:
                data = input('Введите данные для отправки + \n')
                await client.send(data)

                print(await client.recv())





if __name__ == '__main__':
    asyncio.run(Client.Connect())
