class Cachorro:
    """Representa um cachorro com nome e raça."""

    def __init__(self, nome: str, raca: str, idade: int = 0) -> None:
        """
        Inicializa um novo cachorro.
        
        Args:
            nome: Nome do cachorro.
            raca: Raça do cachorro.
            idade: Idade em anos (padrão: 0).
        """
        self.nome = nome      # Atributo de instância
        self.raca = raca      # Atributo de instância
        self.idade = idade    # Atributo de instância
        self.energia = 100    # Atributo com valor fixo inicial


# Criando objetos com argumentos
rex = Cachorro("Rex", "Pastor Alemão", 3)
bob = Cachorro("Bob", "Poodle")

print(f"{rex.nome} é um {rex.raca} de {rex.idade} anos")
# Rex é um Pastor Alemão de 3 anos

print(f"{bob.nome} é um {bob.raca} de {bob.idade} anos")
# Bob é um Poodle de 0 anos