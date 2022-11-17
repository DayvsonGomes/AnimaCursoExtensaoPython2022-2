# passo 1 - importar a biblioteca sqlite3
import Aula4_2022_11_16c as bd

conexao, cursor = bd.conectar()

nome= input("Informe o nome do heroi\vilão: ")
nome_civil= input("Informe o nome civil do heroi\vilão(sua identidade secreta): ")
tipo_numerico = input("Tecle 1 para heróis(na) ou 2 para vilão")

# consulta para o valor máximo usado no banco
sql = "SELECT MAX(pessoa_id) FROM pessoas"
cursor.execute(sql)
pessoa_id = cursor.feltchone()[0]

if tipo_numerico == '1':
  tipo = "Heroí(na)"
else:
  tipo = "Vilã(o)"

sql = f"INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES({pessoa_id}, '{nome}', '{nome_civil}', '{tipo}')"

cursor.execute(sql)
conexao.commit()
