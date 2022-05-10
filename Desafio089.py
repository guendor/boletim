geral = []
individual = []
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    individual.append(nome)
    individual.append(n1)
    individual.append(n2)
    geral.append(individual[:])
    individual.clear()
    resp = str(input('Quer adicionar mais 1 aluno [S/N]? ')).upper().strip()[0]
    if resp in 'N':
        break
print('-=' * 30)
print(f'{"No. NOME":<15} {"MÉDIA":>}')
print('-' * 30)
for a in range(0, len(geral)):
    media = (geral[a][1] + geral[a][2]) / 2
    print('{:<4}{:<1} {:>8.1f}'.format(a, geral[a][0], media))
print('-' * 30)
while True:
    det = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if det == 999:
        print(f'''FINALIZANDO...
{"<<< VOLTE SEMPRE >>>":^30}''')
        break
    print(f'Notas de {geral[det][0]} são {geral[det][1], geral[det][2]}')
    print('-' * 30)
