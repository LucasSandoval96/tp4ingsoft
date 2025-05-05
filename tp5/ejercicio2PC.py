class StringIterator:
    def __init__(self, text):
        self.text = text

    def forward(self):
        for char in self.text:
            yield char

    def backward(self):
        for char in reversed(self.text):
            yield char


# Uso
iterador = StringIterator("hola mundo")

print("Recorrido directo:")
for c in iterador.forward():
    print(c, end=" ")

print("\nRecorrido reverso:")
for c in iterador.backward():
    print(c, end=" ")
