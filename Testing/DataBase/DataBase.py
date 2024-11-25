import json

from mysql.connector import connect, Error


class Connector:
    connects = connect(
            host='localhost',
            user='root',
            password='271126cccccC_'
        )
    cursor = connects.cursor()

    @classmethod
    def Select_User(cls, data: str, parametrs: str):
        cls.cursor.execute(f"SELECT {data} FROM testing.users {parametrs}")
        return cls.cursor.fetchall()[0][0]


    @classmethod
    def Insert_User(cls, group, name):
        cls.cursor.execute(f"INSERT INTO testing.users (NumberGroup,Name) VALUES ('{int(group)}','{str(name)}')")
        cls.connects.commit()

        return True

    @classmethod
    def Update_User(cls, data: tuple, where: str):
        print(f"UPDATE testing.users SET {data}")
        cls.cursor.execute(f"UPDATE testing.users SET {data} WHERE {where}")
        cls.connects.commit()
        return True

    @classmethod
    def Delete_User(cls, data):
        cls.cursor.execute(f"DELETE FROM testing.users WHERE {data} ")
        cls.connects.commit()
        return True


    @classmethod
    def StartTest(cls,group):
        if group == 42215:
            print(json.dumps((["Вопрос №1"], ('1','2','3','4'))))
            return json.dumps((["Вопрос №1"], ('1','2','3','4')))

        return 'Error'

if __name__ == '__main__':
    pass
    #print(Connector.Update_User(("Name = 'Nikita'"),"Name = 'Egor'"))
    #print(Connector.Insert_User(('42215','Egor')))
    #print(Connector.Select_User('*',None))
    #print(Connector.Delete_User("Name='Nikita'"))