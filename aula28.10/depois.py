class Pessoa:
    
     @property
     def idade(self) -> int:
          """Getter: acesso a __idade"""
          print("Passou no getter da idade")
          return self.__idade
     @idade.setter
     def idade(self, valor:int) -> None:
          """Setter: mudar o valor de __idade"""
          print("Passou no setter de idade")
          if valor < 0:
               raise TypeError("Idade impossivel")
          if valor > 100 ("voce está de brincadeira comigo")



p = Pessoa("teste novo", 100)
print("Qual sera a idade dessa pessoa?")
print(p.idade)
p.idade= 50
print("Qual sera a idade dessa pessoa?")
print(p.idade)