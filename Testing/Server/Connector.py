

class Connector:

    @classmethod
    async def OpenFile(cls, data):
        if data == ('42215'):
            # (1-вопросы, 2-варианты ответа, 3-правильный ответ)
            return (('Вопрос №1'),('1', '2', '3', '4'),(1,0,0,0))