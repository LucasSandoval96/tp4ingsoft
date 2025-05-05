class Handler:
    def __init__(self, next_handler=None):
        self.next = next_handler

    def handle(self, number):
        if self.next:
            self.next.handle(number)
        else:
            print(f"{number} no fue consumido.")


class ParHandler(Handler):
    def handle(self, number):
        if number % 2 == 0:
            print(f"{number} consumido por ParHandler")
        else:
            super().handle(number)


class PrimoHandler(Handler):
    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def handle(self, number):
        if self.is_prime(number):
            print(f"{number} consumido por PrimoHandler")
        else:
            super().handle(number)


# Construcción de la cadena: PrimoHandler -> ParHandler
chain = PrimoHandler(ParHandler())

for i in range(1, 101):
    chain.handle(i)
