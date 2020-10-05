# 3. Faça um programa para solicitar o nome e as duas notas e um aluno. Calcular sua média e informá-la. Se ela for
# inferior a 7, escrever "Reprovado”; caso contrário escrever "Aprovado".

nota1 = int(input('informe a primeira nota '))
nota2 = int(input('informe a segunda nota '))

media = (nota1 + nota2)/2


if media >= 7:
    print('APROVADO')
else:
    print('reprovado')