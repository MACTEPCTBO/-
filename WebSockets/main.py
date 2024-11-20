import socket
import time


class Client:
    def __init__(self, IP: str, PORT: int, Name: str):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client.connect((IP,PORT))

        self.client.send(Name.encode())
        time.sleep(1)

        print(f"Connect : {IP}:{PORT}")


    def Send(self, data: str) -> None:
        self.client.send(data.encode())

    def Recv(self) -> str:
        data = self.client.recv(2048).decode()
        print(data)
        return data

a = []

if __name__ == "__main__":
    c = Client('127.0.0.1',3000,'Egor')
    c.Send('1234')
    c.Recv()
