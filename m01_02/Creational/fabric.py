from abc import ABC, abstractmethod
from enum import Enum
from typing import List


class TypeOperation(str, Enum):
    SUM = 'sum'
    MUL = 'mul'


class Operation(ABC):
    def __init__(self):
        self.data = None

    @abstractmethod
    def operation(self):
        pass

    @abstractmethod
    def info(self):
        pass


class Adder(Operation):
    def __init__(self, data: List[int]):
        super().__init__()
        self.data = data

    def operation(self):
        return sum(self.data)

    def info(self):
        return TypeOperation.SUM.value


class Multiplier(Operation):
    def __init__(self, data: List[int]):
        super().__init__()
        self.data = data

    def operation(self):
        mul = 1
        for el in self.data:
            mul *= el
        return mul

    def info(self):
        return TypeOperation.MUL.name


class Factory(ABC):
    @abstractmethod
    def create_operation(self) -> Operation:
        pass

    def make_operation(self) -> Operation:
        operation = self.create_operation()
        return operation


class SumFactory(Factory):
    def __init__(self, data: List[int]):
        self.data = data

    def create_operation(self) -> Operation:
        return Adder(self.data)


class MulFactory(Factory):
    def __init__(self, data: List[int]):
        self.data = data

    def create_operation(self) -> Operation:
        return Multiplier(self.data)


def calculation(factory: Factory):
    operator = factory.make_operation()
    result = operator.operation()
    return result, operator.info(), operator.data


if __name__ == '__main__':
    data = [34, 22, 11, 23, 11, 2]
    print(calculation(SumFactory(data)))
    print(calculation(MulFactory(data)))
