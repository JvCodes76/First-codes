def soma(x, y):
    resultado = x + y
    return resultado

def subtracao (x, y):
    resultado = x - y
    return resultado

def multiplicacao(x, y):
    resultado = x*y
    return resultado

def divisao (x, y):
    if y != 0:
        return x/y
    else:
        return 'Indeterminado'

def exponenciacao(x, y):
    resultado = x**y
    return resultado

def restoDaDivisao(x, y):
    if y != 0:
        return x%y
    else:
        return 'Indeterminado'
    
operando1 = int(input('Primeiro operando: '))
operador = int(input('Digite o numero da operação deseajada \n1 = soma \n2 = aubtração\n3 = multiplicação\n4 = divisão\n5 = exponenciação\n6 = resto da divisão\ninput: '))
operando2 = int(input('Segundo operando: '))
if operador == 1:
    result = soma(operando1, operando2)
    print(f'\nresultado = {result}')
elif operador == 2:
    result = subtracao(operando1, operando2)
    print(f'\nresultado = {result}')
elif operador == 3:
    result = multiplicacao(operando1, operando2)
    print(f'\nresultado = {result}')
elif operador == 4:
    result = divisao(operando1, operando2)
    print(f'\nresultado = {result}')
elif operador == 5:
    result = exponenciacao(operando1, operando2)
    print(f'\nresultado = {result}')
elif operador == 6:
    result = restoDaDivisao(operando1, operando2)
    print(f'\nresultado = {result}')