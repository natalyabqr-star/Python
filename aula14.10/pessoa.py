class Pessoa:
    def __init__(self, nome:str, idade: int) -> None:
        self.nome = nome 
        self.idade = idade

fulano = Pessoa("fulano", 25)
print(fulano.nome)
fulano.idade = -5
print(fulano.idade)