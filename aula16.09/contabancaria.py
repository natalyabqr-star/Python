class ContaBancaria:
    """Representa uma conta bancária simplificada."""

    def __init__(self, titular: str, saldo_inicial: float = 0.0) -> None:
        """
        Cria uma nova conta bancária.
        
        Args:
            titular: Nome do titular da conta.
            saldo_inicial: Saldo inicial (padrão: 0).
        """
        self.titular = titular
        self.saldo = saldo_inicial
        self.ativa = True
        self.historico: list[str] = []

    def depositar(self, valor: float) -> bool:
        """
        Realiza um depósito na conta.
        
        Args:
            valor: Valor a depositar (deve ser positivo).
        
        Returns:
            True se o depósito foi realizado, False caso contrário.
        """
        if not self.ativa:
            print("Conta inativa! Operação negada.")
            return False
        
        if valor <= 0:
            print("Valor de depósito deve ser positivo!")
            return False
        
        self.saldo += valor
        self.historico.append(f"Depósito: +R${valor:.2f}")
        print(f"✓ Depósito de R${valor:.2f} realizado.")
        return True

    def sacar(self, valor: float) -> bool:
        """
        Realiza um saque da conta.
        
        Args:
            valor: Valor a sacar.
        
        Returns:
            True se o saque foi realizado, False caso contrário.
        """
        if not self.ativa:
            print("Conta inativa! Operação negada.")
            return False
        
        if valor <= 0:
            print("Valor de saque deve ser positivo!")
            return False
        
        if valor > self.saldo:
            print(f"Saldo insuficiente! Disponível: R${self.saldo:.2f}")
            return False
        
        self.saldo -= valor
        self.historico.append(f"Saque: -R${valor:.2f}")
        print(f"✓ Saque de R${valor:.2f} realizado.")
        return True

    def transferir(self, destino: "ContaBancaria", valor: float) -> bool:
        """
        Transfere valor para outra conta.
        
        Args:
            destino: Conta de destino.
            valor: Valor a transferir.
        
        Returns:
            True se a transferência foi realizada.
        """
        if self.sacar(valor):
            destino.depositar(valor)
            self.historico.append(f"Transferência para {destino.titular}: -R${valor:.2f}")
            destino.historico.append(f"Recebido de {self.titular}: +R${valor:.2f}")
            return True
        return False

    def extrato(self) -> None:
        """Exibe o extrato da conta."""
        print(f"\n{'=' * 35}")
        print(f"  EXTRATO - {self.titular}")
        print(f"{'=' * 35}")
        
        if self.historico:
            for registro in self.historico:
                print(f"  {registro}")
        else:
            print("  Sem movimentações.")
        
        print(f"{'─' * 35}")
        print(f"  Saldo atual: R${self.saldo:.2f}")
        print(f"{'=' * 35}")


# === Uso ===
conta_maria = ContaBancaria("Maria", 1000.0)
conta_joao = ContaBancaria("João", 500.0)

conta_maria.depositar(200)
conta_maria.sacar(50)
conta_maria.transferir(conta_joao, 300)

conta_maria.extrato()
conta_joao.extrato()