def soma(x, y):
    return x + y 

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: Divisão por Zero!"
    
    def calculadora():
        print("Selecione a operaçao:")
        print("1. soma")
        print("2. subtração")
        print("3. multiplicação")
        print("4. Divisão")

escolha = input("Digite sua escolha (1/2/3/4):")

num1 = float(input("Digite o primeiro numero:"))
num2 = float(input("Digite o segundo numero:"))

if escolha == '1':
    print(f"{num1} + {soma(num1, num2)}")

elif escolha == '2':
    print(f"{num1} - {num2} = {subtracao(num1, num2)}")

elif escolha == '3':
    print(f"{num1} * {num2} = {multiplicacao(num1, num2)}")

elif escolha == '4':
    resultado = divisao(num1, num2)
    print(f"{num1} / {num2} = {resultado}")

else:
    print("Opção invalida!")


calculadora()