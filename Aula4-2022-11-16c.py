# passo 1 - importar a biblioteca sqlite3
import sqlite3

# passo 2: vamos estabelecer uma conexão com o banco
conexao=sqlite3.connect("dc_universe.db")

# passo 3: criar um objeto do tipo cursor
cursor = conexao.cursor()

# passo4: Comando SQL do banco
sql = "SELECT pessoa_id, nome,nome_civil, tipo FROM pessoas"

# passo 5: colocar o camando SQL dentro da variavel String
cursor.execute(sql)

# passo 6: exibir a consulta com todos os nomes de heróis e vilões
pessoas = cursor.fetchall()
for pessoa in pessoas:
  print(pessoa)

for pessoa in pessoas:
  print(f'Nome:{pessoa[1]}({pessoa[2]})')

