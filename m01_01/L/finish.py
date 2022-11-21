# from __future__ import annotations

from abc import abstractmethod, ABC

"""
В этом примере нарушен принцип подстановки Лисков (далее LSP) - принцип при построении иерархии наследования классов в 
объектно-ориентированных языках программирования. По сути, правильная иерархия наследования в ООП — это иерархия, 
построенная согласно LSP, чтобы отвечать принципу открытости-закрытости.

Появление класса SMS приводит к изменению класса NotificationService
"""


class Notification(ABC):
    @abstractmethod
    def notify(self, message):
        pass


class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


class Email(Notification):
    def __init__(self, email):
        self.email = email

    def notify(self, message):
        print(f"Send {message} to email: {self.email}")


class SMS(Notification):
    def __init__(self, phone):
        self.phone = phone

    def notify(self, message):
        print(f"Send {message} sms to phone: {self.phone}")


class NotificationService:
    def __init__(self, notification: Notification):
        self.notification = notification

    def send(self, message):
        self.notification.notify(message)


if __name__ == "__main__":
    person = Contact("Dima", "dima@gmail.com", "+380663332211")
    notify_SMS = SMS(person.phone)
    notify_email = Email(person.email)
    service_SMS = NotificationService(notify_SMS)
    service_SMS.send("Hello bro!")
    service_email = NotificationService(notify_email)
    service_email.send("Hello bro!")
