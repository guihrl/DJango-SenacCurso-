import sqlite3

#Criando conexão com o banco de dados
conn = sqlite3.connect('mydatabase.db')

#Atualizar dados na tabela
escolher = input("Digite o preço que deseja atualizar: ")
conn.execute(f"UPDATE stocks SET price = {escolher} WHERE symbol = 'RHAT'")

#Salvar as alterações
conn.commit()

#Fechar a conexão com o banco de dados
conn.close()
