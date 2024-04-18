import mysql.connector
try:
    conection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        database="banco"
    )
    
    marca_prod=str(input("Digite a marca do produto: "))
    nome_prod=str(input("Digite o nome do prduto: "))
    valor_custo=float(input("Digite o custo do produto: "))
    valor_venda=float(input("Digite o valor de venda do produto: "))

    sql="INSERT INTO produtos (marca_produto, nome_produto, valor_custo, valor_venda) VALUES (%s,%s,%s,%s)"
    cursor=conection.cursor()
    cursor.execute (sql, (marca_prod,nome_prod,valor_custo,valor_venda))
    conection.commit()
    cursor.close()
    conection.close()

except Exception as e:
    print(f"Erro ao salvar dados: {e}")