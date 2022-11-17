# passo 1 - importar a biblioteca sqlite3
import sqlite3

# passo 2 e 3: virarão funçao conectar
def conectar():
  # passo 2: cestabelecer conexao com o BD
  conexao=sqlite3.connect("dc_universe.db")

  # passo 3: criar um objeto to tipo cursor
  cursor = conexao.cursor()

  return conexao, cursor

