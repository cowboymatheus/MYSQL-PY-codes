import mysql.connector
try:
    conection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        database="banco"
    )

    print("(1) Deletar linha da tabela 'Clientes'")
    print("(2) Deletar linha da tabela 'Produtos'")
    print("(3) Deletar linha da tabela 'Pedidos'")
    option = int(input(f"Digite o número da sua opção: "))
    id_linha_a_ser_del = int(input(f"Digite o ID da linha que deseja deletar: "))
    cursor=conection.cursor()

    if option == 1:
        print("------------------------------")
        cursor.execute("DELETE FROM clientes WHERE id_cliente = %s", (id_linha_a_ser_del,))
        conection.commit()
        print("Linha da tabela Clientes deletada com sucesso!")
        print("------------------------------")

    if option == 2:
        print("------------------------------")
        cursor.execute("DELETE FROM produtos WHERE id_produto = %s", (id_linha_a_ser_del,))
        conection.commit()
        print("Linha da tabela Produtos deletada com sucesso!")
        print("------------------------------")

    if option == 3:
        print("------------------------------")
        cursor.execute("DELETE FROM pedidos WHERE id_pedido = %s", (id_linha_a_ser_del,))
        conection.commit()
        print("Linha da tabela Produtos deletada com sucesso!")
        print("------------------------------")


except Exception as e:
    print(f"Erro ao salvar dados: {e}")