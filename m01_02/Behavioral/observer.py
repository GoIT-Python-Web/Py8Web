import datetime


class Event:
    _observers = []

    def register(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def unregister(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_all(self, event: str, data=None):
        for observer in self._observers:
            observer(event, data)


# Додаємо слухачів
def terminal_logger(event: str, data):
    print(event, data)


class FileLogger:
    def __init__(self, filename):
        self.filename = filename

    def __call__(self, event: str, data):
        with open(self.filename, 'a') as fl:
            fl.write(f"{datetime.datetime.now()}: [{event}] - {data}\n")


if __name__ == '__main__':
    event = Event()

    event.register(terminal_logger)
    flog = FileLogger('streams.log')
    event.register(flog)

    event.notify_all('tick', 122)
    event.notify_all('tick', 123)
    event.notify_all('tick', 124)
    event.notify_all('message', 'Sometime it happens')
    event.unregister(flog)
    event.notify_all('tick', 125)
    event.unregister(terminal_logger)
    event.notify_all('tick', 126)
    event.notify_all('tick', 127)
