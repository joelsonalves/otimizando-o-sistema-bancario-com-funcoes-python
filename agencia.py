from conta import Conta
from cliente import Cliente

class Agencia:

    def __innit__(self, numero):

        self.numero = numero
        self.contas = []

    def abrir_conta(self, numero, cliente):

        if self.localizar_conta(numero):
            print('@@@ Conta já cadastrada.')
        
        else:
            nova_conta = Conta(numero, cliente)
            self.contas.append(nova_conta)
            print('### Conta cadastrada com sucesso.')

    def localizar_conta(self, numero):

        for c in self.contas:
            if c.numero == numero:
                return c
        
        return None