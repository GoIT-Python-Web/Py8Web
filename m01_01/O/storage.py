from abc import ABC, abstractmethod
import json
import yaml


class Storage(ABC):
    @abstractmethod
    def get_value(self, key):
        pass


class JSONStorage(Storage):
    def __init__(self, filename):
        self.filename = filename

    def get_value(self, key):
        with open(self.filename, 'r') as f:
            data = json.load(f)
            return data.get(key, None)


class YamlStorage(Storage):
    def __init__(self, filename):
        self.filename = filename

    def get_value(self, key):
        with open(self.filename, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            return data.get(key, None)
