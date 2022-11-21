from abc import abstractmethod, ABC


class IPerson(ABC):
    @abstractmethod
    def get_phone_number(self):
        pass


class IPhone(ABC):
    @abstractmethod
    def value_of(self):
        pass


class PhoneNumber(IPhone):
    def __init__(self, phone: str, operator_code: str):
        self.phone = phone
        self.operator_code = operator_code

    def value_of(self):
        return f"+38({self.operator_code}){self.phone}"


class PersonAddress:
    def __init__(self, zip, city, street):
        self.zip = zip
        self.city = city
        self.street = street

    def value_of(self):
        return f'{self.zip}, {self.city}, {self.street}'


class Person(IPerson):
    def __init__(self, name: str, phone: IPhone, address: PersonAddress):
        self.name = name
        self.phone = phone
        self.address = address

    def get_phone_number(self):
        return f"{self.name}: {self.phone.value_of()}"

    def get_address(self):
        return self.address.value_of()


if __name__ == '__main__':
    person = Person("Alexander", PhoneNumber("9995544", "050"), PersonAddress('36007', 'Poltava', 'European, 28'))
    print(person.get_phone_number())
    print(person.get_address())


# Согласно принципу Single responsibility выделить класс для телефона (адреса). Добавить абстракции
