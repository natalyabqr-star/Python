aluno1_nome = "fulano"
aluno1_idade = 20
aula1_notas = [10,0,0]


aluno2_nome = "fulana"
aluno2_idade = 22
aula2_notas = [10,10,10]


def calcular_media(notas:list[float]) -> float:
    return sum(notas) / len(notas) if notas else 0.0