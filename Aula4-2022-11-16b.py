# passo 1 - importar a biblioteca sqlite3
import sqlite3

# passo 2: vamos estabelecer uma conexão com o banco
conexao=sqlite3.connect("dc_universe.db")

# passo 3: criar um objeto do tipo cursor
cursor = conexao.cursor()

# passo 4: Comando para inserir um heroi/vilão
sql = "INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES(12,'The Flash','Barry Allen','Herói(na)')"

# passo 5: Executar o comando SQL
print(cursor.execute(sql))

# passo 6: Confirmar o INSERT com o commit e  fechar o banco
conexao.commit()
conexao.close()

