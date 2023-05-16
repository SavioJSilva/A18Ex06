ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    r1 = str(input('Quer continuar? [S/N] '))
    if r1 in 'Nn':
        break
print('--' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÈDIA":>8}')
print('--' * 30)
for indice, alunos in enumerate(ficha):
    print(f'{indice:<4}{alunos[0]:<10}{alunos[2]:>8.1f}')
while True:
    print('--' * 30)
    r2 = int(input('Deseja visualizar a nota de algum aluno especifico? Se sim, Qual? (999 para parar): '))
    if r2 == 999:
        print('Até mais!')
        break
    if r2 <= len(ficha) - 1:
        print(f'Notas de {ficha[r2][0]} são {ficha[r2][1]}')
print('--' * 10, 'Volte sempre!', '--' * 10)