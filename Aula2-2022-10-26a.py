#Pede o nome do aluno e sua nota (de 0 a 10) e, se ele tirou nota 10, mostra "Você é bichão, mesmo..."

nome = input('informe seu nome: ')
nota = float(input('Digite sua nota: '))

if nota == 10:
  print(f' {nome} Você é bixão mesmo...')
elif nota >=6 and nota <10:
  print(f'Sua nota é {nota}, BOM TRABALHO!')
else:
  print('Não tirou a nota desejada.')