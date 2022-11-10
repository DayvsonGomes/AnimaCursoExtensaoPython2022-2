#  criação de funçoes 

preco = 1999.90

# calcular 5% de imposto, guardar na variavel imposto e exibir na tela

imposto = preco * 0.05
print(imposto)

preco2 = 100
imposto2 = preco2 *0.05
print(imposto)

#Criar uma função calcular_imposto() que calcula um imposto de 5% e retorna quem pediu
# Isso é a declaração da função
def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.05
  return imposto

#Aqui é o uso... aqui é o imposto a calcular...
preco = 299
calcular_imposto(preco)
print(f' Esse aqui é com a função (7%): {imposto}')


print(preco)
preco_produto = 100
print(preco_produto)

valores = [200, 350, 500, 750]
#Agora calcular o imposto destes quatro valores... e exibir na tela assim: "O imposro de .... é .....(io, preço, 2o, imposto)"

for valor in valores:
  print(f' O imposto de {valor} é {calcular_imposto}(valor)')

#Declarar uma função calcula_imposto_aliquota que recebe dois parametros: o preço do produto e a alíquota de imposto a ser aplicada e retorna o imposto calculado. Se a Aliquota não for informada, utilize 7% como padrão.

def calcular_imposto_aliquota(valor, aliquota=7):
  imposto= valor *aliquota / 100
  return imposto
  
for valor in valores:
  print(f' O imposto de {valor} é {calcular_imposto_aliquota(valor,7)}')  


