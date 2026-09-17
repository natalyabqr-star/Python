class Circulo:
    """Representa um círculo."""

    def __init__(self, raio: float) -> None:
        self.raio = raio  # 'self.raio' é o atributo do objeto

    def area(self) -> float:
        """Calcula a área do círculo."""
        return 3.14159 * self.raio ** 2  # Acessa o atributo via self

    def perimetro(self) -> float:
        """Calcula o perímetro do círculo."""
        return 2 * 3.14159 * self.raio

    def redimensionar(self, fator: float) -> None:
        """Redimensiona o círculo por um fator."""
        self.raio *= fator


# Uso
c1 = Circulo(5)
c2 = Circulo(3)

print(f"Círculo 1: raio={c1.raio}, área={c1.area():.2f}")
# Círculo 1: raio=5, área=78.54

print(f"Círculo 2: raio={c2.raio}, área={c2.area():.2f}")
# Círculo 2: raio=3, área=28.27

c1.redimensionar(2)
print(f"Após redimensionar: raio={c1.raio}, área={c1.area():.2f}")
# Após redimensionar: raio=10, área=314.16