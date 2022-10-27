# comando input(): quero perimitir
#  que o usua=ário digite algo
nome= input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
idade2 = (int(idade *2))
genero = input('Informe o gênero M=Masculino, F=Feminino, O=Outros: ')
print(f'Seu nome é {nome} e você tem {idade} anos.\n')
print(f'O dobro da sua idade é {idade2} anos.\n')
#  mostrando o nome e idades acima

#  Estrutura condicional 'se'
#  Se a pessoa for maior de idade, mostre 'Voce ja pode dirigir'
if (idade >=18 and genero == 'M'):
  print('e voce também precisa/ precisou prestar o seviço militar.\n')
  
elif(genero == 'F'):
  print('Você não pode beber e nem dirigir.')

# E se eu quisesse perguntar o gênero(Masculino e femninino
#Mostre... e voce também precisa/ precisou prestar o seviço militar)