# -*- coding: utf-8 -*-

def AguaIndiv(peso):
    return peso*35/1000

contador = 0
conta2l = 0
conta3l = 0
somaLitros = 0
somaPeso3l = 0
numeroDeAlunos = int(input('Número de alunos na sala '))
while contador != numeroDeAlunos:
    contador+=1
    peso = int(input(f'Qual o peso em kg do aluno {contador} '))
    print(f'Quantidade de água recomendada para o aluno {contador} = {AguaIndiv(peso)}L ')
    somaLitros+= AguaIndiv(peso)
    if AguaIndiv(peso) <= 2:
        conta2l+=1
    if AguaIndiv(peso) >= 3:
        conta3l+=1
        somaPeso3l+=peso

mediaPeso3l = somaPeso3l/numeroDeAlunos
porcent2L = conta2l*100/numeroDeAlunos
media = somaLitros/numeroDeAlunos
print(f'Alunos que precisam beber menos de 2 litros de água = {conta2l}')
print(f'Porcentagem de alunos que precisam beber menos de 2L = {porcent2L}')
print(f'Soma total de litros recomendados para a turma = {somaLitros}')
print(f'Média da turma = {media}')
print(f'Média de peso dos alunos que tem recomedação de ingrestão de água maior ou igual a 3L = {mediaPeso3l}')



    

