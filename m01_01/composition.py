from abc import abstractmethod, ABC


class Animal(ABC):
    def __init__(self, nickname, age):
        self.nickname = nickname
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Owner:
    def __init__(self, name: str, phone: str):
        self.name = name
        self.phone = phone

    def get_info(self):
        return f"{self.name}: {self.phone}"


class Cat(Animal):
    def __init__(self, nickname, age, name: str, phone: str):
        super().__init__(nickname, age)
        self.owner = Owner(name, phone)

    def get_info(self):
        return f"This is cat. His name is {self.nickname}, age: {self.age}:"


if __name__ == '__main__':
    cat = Cat('Kurt', 5, 'Max', '104')
