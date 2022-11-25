class Settings:
    """Classic singleton"""

    __instance = None

    def __init__(self):
        self.db = 'postgres://localhost'
        self.port = 5634

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(Settings)
        return cls.__instance


class NewSettings(Settings):
    pass


if __name__ == '__main__':

    connect = Settings()
    print(connect.port)

    other_connect = Settings()
    print(other_connect.port)
    other_connect.port = 3306

    print(other_connect.port, connect.port)

connect_ = NewSettings()
print(connect_.port)
