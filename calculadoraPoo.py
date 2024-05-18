#
class Calculadora:
    def __init__(self):
        print("Calculadora criada!")
    
    def somar(self, num1, num2):
        return num1 + num2
    
    def subtrair(self, num1, num2):
        return num1 - num2

    def multiplicar(self, num1, num2):
        return num1 * num2
    
    def dividir(self, num1, num2):
        if (num2 == 0):
            return "Divisão por 0 não é impossível"
        else:
            return num1 / num2

#instanciando o objeto
calculadoraJuvenaldo = Calculadora()
print(calculadoraJuvenaldo.somar(2,2))
        