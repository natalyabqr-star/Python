class Pessoa:
     def __init__(self, nome: str, idade:int) -> None
     self.__nome = nome
     self.__idade = idade


    @property
    def nome(self) -> str:
        """Getter: acesso ao __nome"""
        return self.__idade

    def idade(self, valor: int) -> None:
     """Setter: muda o valor de __idade"""

     if valor < 0:
         raise TypeError("idade impossivel")

     if valor < 100:
         raise TypeError("voce ta de brincadeira") 


p = Pessoa("teste novo", 100)
print("Qual sera a idade dessa pessoa?")
print(p.idade)
p.idade= 50
print("Qual sera a idade dessa pessoa?")
print(p.idade)