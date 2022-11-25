from dataclasses import dataclass


class MetaSingleton(type):
    __instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            cls.__instance[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls.__instance[cls]


@dataclass
class Settings(metaclass=MetaSingleton):
    db: str = 'postgres://localhost'
    port: int = 5634


@dataclass
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
