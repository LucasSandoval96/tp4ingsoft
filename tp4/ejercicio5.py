class Caracter:
    def __init__(self, simbolo):
        self.simbolo = simbolo

    def mostrar(self, fuente):
        print(f"{self.simbolo} en fuente {fuente}")

class FabricaCaracteres:
    _caracteres = {}

    @classmethod
    def obtener(cls, simbolo):
        if simbolo not in cls._caracteres:
            cls._caracteres[simbolo] = Caracter(simbolo)
        return cls._caracteres[simbolo]

# Ejemplo
texto = "hola mundo hola"
for c in texto.replace(" ", ""):
    char = FabricaCaracteres.obtener(c)
    char.mostrar("Arial")
