from storage import JSONStorage, YamlStorage, Storage


class ServiceStorage:
    def __init__(self, storage: Storage):
        self.storage = storage

    def get(self, key):
        return self.storage.get_value(key)


if __name__ == '__main__':
    marketing_storage = ServiceStorage(YamlStorage('data.yaml'))
    hr_storage = ServiceStorage(JSONStorage('data.json'))

    print(marketing_storage.get('username'))
    print(hr_storage.get('username'))
