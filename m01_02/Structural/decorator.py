class Greeting:
    def __init__(self, username: str) -> None:
        self.username = username

    def greet(self):
        return f"Hello {self.username}"


class GreetingDecorator:
    def __init__(self, wrapper: Greeting) -> None:
        self.wrapper = wrapper

    def greet(self):
        base_greet = self.wrapper.greet()
        return f"{base_greet.upper()}!"


if __name__ == '__main__':
    message = GreetingDecorator(Greeting('Spod'))
    print(message.greet())
