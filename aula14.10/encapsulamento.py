class Cofre:
    def __init__(self, senha:str) -> None:
     self.__senha = senha 
     self.__tentativa = 0


    def abrir(self, senha:str) -> bool:
        """Tentar abrir o cofre com a senha fornecida"""
        self.__tentativa += 1

        if senha == self.__senha:
            print("Cofre aberto")
            return True 

        print(f"Senha invalida! Você exedeu a suas tentativas {self.__tentativa}")
        return False 

    def trocar_senha(self, senha_atual:str, nova_senha:str) -> bool:
       """Trocar a senha do cofre"""
       if senha_atual == self.__senha:
          self.__senha = nova_senha
          print("Senha alterada")
          return True

       print("Senha informada invalida")
       return False


cofre = Cofre("abc123")
cofre.abrir("errado")
cofre.abrir("abc123")