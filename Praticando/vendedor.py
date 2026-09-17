#Criamos uma classe do usuario e atribui informações dele, que ele pode fazer, e dar essas regras para o sistema, criamos um sistema com essa regra, e quando o cliente clicar em algopode executamos uma função dessas.
class Vendedor():
    def __init__(self, nome):
        self.nome = nome
        self.vendas = 0

    def vendeu(self, vendas):
        self.vendas = vendas

    def bateu_meta(self, meta):
        if self.vendas > meta:
            print(self.nome, "você bateu a meta parabéns, isso significa que irá ter aumento no seu salário esse mês!!!")
        elif self.vendas >= meta:
            print(self.nome, "bateu a meta, porém não foi o suficiente")
        else:
            print(self.nome, "você não bateu a meta, infelizmente por conta de leis da empresa, teramos que descontar 1% do seu salário, sinto muito")
        


Vendedor1 = Vendedor("Fulano")
Vendedor1.vendeu(1000)
Vendedor1.bateu_meta(600)

Vendedor2 = Vendedor("Bia")
Vendedor2.vendeu(50)
Vendedor2.bateu_meta(100)

Vendedor3 = Vendedor("Carla")
Vendedor3.vendeu(90)
Vendedor3.bateu_meta(100)

