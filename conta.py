from cliente import Cliente

class Conta:

    def __init__(self, numero, cliente):

        self.numero = numero
        self.cliente = cliente
        self.saldo = 0.00
        self.movimentacao = ''

    def depositar(self, valor):

        if type(valor) == float and valor > 0:
            self.movimentacao += f'Saldo: R$ {self.saldo:.2f}\n\n'
            self.saldo += valor
            self.movimentacao += f'Depósito de R$ {valor:.2f} (+)\n\n'
            print('### Depósito realizado com sucesso.')
        
        else:
            print('@@@ Não foi possível realizar o depósito.')

    def sacar(self, valor):
        
        if type(valor) == float and valor > 0 and self.saldo >= valor:
            self.movimentacao += f'Saldo: R$ {self.saldo:.2f}\n\n'
            self.saldo -= valor
            self.movimentacao += f'Saque de R$ {valor:.2f} (-)\n\n'
            print('### Saque realizado com sucesso.')

        else:
            print('@@@ Não foi possível realizar o saque.')

    def exibir_extrato(self):

        print(f'Conta Corrente nº {str(self.numero).zfill(4)}\n')
        print('$$$$$$$ Extrato $$$$$$$\n')
        print(self.movimentacao)
        print(f'Saldo Atual: R$ {self.saldo:.2f}')