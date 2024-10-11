import sqlite3

#Criando conexão com o banco de dados
conn = sqlite3.connect('mydatabase.db')

#Selecionar todos os dados da tabela
cursor = conn.execute("SELECT * FROM stocks")

#Iterar sobre os dados e exibir-los
for row in cursor:
    print(row)
    
#Fechar a conexão com o banco de dados
conn.close()
