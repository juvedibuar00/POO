class ContaBancaria:
    #CONSTRUÇÃO DO OBJETO CONTA BANCARIA
    def __init__(self, titular, saldo:float=0):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valorDepositado:float):
        self.saldo = self.saldo + valorDepositado
        
    def sacar(self, valorSacado):
        self.saldo = self.saldo - valorSacado
    
    def consultarSado(self):
        '''Retorna um texto com o titular da conta e o valor'''
        return(f'A conta do titular {self.titular} tem R$ {self.saldo}')

contaJoao = ContaBancaria('Joao Vicente', 5000.00)

print(contaJoao.consultarSado())