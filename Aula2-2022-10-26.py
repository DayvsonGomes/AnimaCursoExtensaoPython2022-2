#Pede o nome do aluno e sua nota (de 0 a 10) e, se ele tirou nota 10, mostra "Você é bichão, mesmo..."

nome = input('informe seu nome: ')
nota = int(input('Digite sua nota; '))

if nota == 10:
  print(f' {nome}Você é bixão mesmo...')
elif nota <= 9:
  print(f'sua nota é {nota}')