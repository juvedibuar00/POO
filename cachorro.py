#CARACTERISTICAS: Temperamento, tamanho, cor, nome
#Ações do cachorro (métodos): latir, pular, correr, comer

class Cachorro:
    #metodo construtor
    def __init__(self, temperamento, tamanho, raca, cor, nome):
        self.nome = nome
        self.temperamento = temperamento
        self.tamanho = tamanho
        self.raca = raca
        self.cor = cor
    def latir(self):
        print(f'{self.nome} está latindo')
cachorro1 = Cachorro('dócil', 'pequno', 'SRD', 'Preto e cinza', 'Nick')

cachorro1.latir()
print(cachorro1.temperamento)
