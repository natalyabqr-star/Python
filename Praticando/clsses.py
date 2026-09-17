#Aqui podemos criar uma nova pasta e nomea-lá como classes, que irá ser a nossas regras para o usúario
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
        