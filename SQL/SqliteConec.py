import sqlite3

#Criando conexão com o banco de dados
conn = sqlite3.connect('mydatabase.db')

#Criar uma tabela
conn.execute('''CREATE TABLE stocks (date text,  trans text, symbol text, qty real, price real)''')

#Salvar as alterações
conn.commit()

#Fechar a conexão com o banco de dados
conn.close()

