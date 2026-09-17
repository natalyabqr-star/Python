class Aluno:
    """Representa um aluno no sistema academico"""

    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade
        self.notas: list[float] = []


    def adicionar_nota(self, nota: float) -> None:
        """Adcionar uma nota (com validação)"""

        if 0 <= nota <= 10:
            self.notas.append(nota)
        else:
            print(f"Nota somente permitida a parmera")


    def calcular_media(self) -> float:
        """Calcular a media das notas"""

        return sum(self.notas) / len(self.notas) if self.notas else 0.0


    def situacao(self) -> str:
        """Retorna a situação de aprovado ou reprovado do aluno"""

        media = self.calcular_media()
        return "Aprovado" if media >= 7.0 else "Reprovado"




aluno1 = Aluno("fulano", 20)
aluno1.adicionar_nota(8)
aluno1.adicionar_nota(9)
aluno1.adicionar_nota(10)

print(f"{aluno1.nome}: {aluno1.situacao()}")

aluno2 = Aluno("Parmera", 40)
aluno2.adicionar_nota(0)
aluno2.adicionar_nota(1)
aluno2.adicionar_nota(0.5)

print(f"{aluno2.nome}: {aluno2.situacao()}")