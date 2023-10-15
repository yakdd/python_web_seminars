class MyException(Exception):
    def __init__(self, msg: str):
        self.msg = msg

    def __str__(self):
        return f'MyException: {self.msg}'


class AccessError(MyException):
    def __init__(self, msg):
        super().__init__(msg)
