import sqlite3

conn = sqlite3.connect('ofina.db')

def criar_tabela():
    conn.execute('''CREATE TABLE oficina_do_seu_zé (date text,  trans text, symbol text, qty real, price real)''')
    conn.commit()

    
def inserir_dados():
    data = input("Data exata da compra ou venda: ")
    compra = input("Insira se foi comprado ou vendido: ")
    marca = input("Insira qual é a marca de pneu: ")
    qntd = input("Insita a quantidade de pneus")
    valor = input(".")
    conn.execute("INSERT INTO oficina_do_seu_zé VALUES ('2024-01-05','COMPRADO','Michelin', 16 ,2434.14)")

    conn.commit()

def Ler_dados():
    cursor = conn.execute("SELECT * FROM oficina_do_seu_zé")
    for row in cursor:
        print(row)
        
def Atualizar_dados():
    escolher = input("Digite o preço que deseja atualizar: ")
    conn.execute(f"UPDATE oficina_do_seu_zé SET price = {escolher} WHERE symbol = 'Pirelli'")
    
def Deletar_dados():
    conn.execute("DELETE FROM oficina_do_seu_zé WHERE symbol = 'Goodyear'")
    
criar_tabela()
inserir_dados()
Ler_dados()
Atualizar_dados()
Deletar_dados()

conn.close()