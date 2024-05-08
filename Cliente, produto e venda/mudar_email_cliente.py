import mysql.connector
try:
    conection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        database="banco"
    )

    id_cliente_p_mudar_email=str(input("Digite o ID do cliente que deseja mudar de email: "))
    novo_email=str(input("Digite o novo email do cliente: "))

    cursor=conection.cursor()

    cursor.execute("SELECT id_cliente FROM clientes WHERE id_cliente = %s", (id_cliente_p_mudar_email,))
    client = cursor.fetchone()

    if not client:
        print("Erro: Cliente não encontrado.")
        conection.close()
        exit()

    sql="UPDATE clientes SET email_cliente = %s WHERE id_cliente = %s"
    cursor.execute (sql, (novo_email, id_cliente_p_mudar_email))
    conection.commit()
    cursor.close()
    conection.close()

except Exception as e:
    print(f"Erro ao salvar dados: {e}")