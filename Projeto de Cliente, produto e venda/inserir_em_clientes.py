import mysql.connector
try:
    conection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        database="banco"
    )
    
    nome=str(input("Digite o nome do cliente: "))
    email=str(input("Digite o email do cliente: "))
    tel=str(input("Digite o telefone do cliente: "))

    sql="INSERT INTO clientes (nome_cliente, email_cliente, tel_cliente) VALUES (%s,%s,%s)"
    cursor=conection.cursor()
    cursor.execute (sql, (nome,email,tel))
    conection.commit()
    cursor.close()
    conection.close()

except Exception as e:
    print(f"Erro ao salvar dados: {e}")