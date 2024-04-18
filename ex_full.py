import mysql.connector
try:
    conection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        database="banco"
    )
    
    print("(1) Listar clientes")
    print("(2) Listar produtos")
    print("(3) Listar vendas")
    print("(4) Cadastrar cliente")
    print("(5) Cadastrar produto")
    print("(6) Cadastrar pedido")
    print("(7) Mudar valores de um produto")
    print("(8) Deletar linha de uma tabela")
    option = int(input(f"Digite o número da sua opção: "))

    #opção 1
    if option == 1:
        cursor=conection.cursor()
        sql = "SELECT * FROM clientes"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        conection.commit()
        cursor.close()
        conection.close()

        for resultado in resultados:
            print(f"{resultado}/n")
    
    #opção 2
    elif option == 2:
        cursor=conection.cursor()
        sql = "SELECT * FROM produtos"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        conection.commit()
        cursor.close()
        conection.close()

        for resultado in resultados:
            print(f"{resultado}/n")
    
    #opção 3
    elif option == 3:
        cursor=conection.cursor()
        sql = "SELECT * FROM pedidos"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        conection.commit()
        cursor.close()
        conection.close()

        for resultado in resultados:
            print(f"{resultado}/n")

    #opção 4
    elif option == 4:
        print("-----------------------------------------------")
        nome=str(input("Digite o nome do cliente: "))
        email=str(input("Digite o email do cliente: "))
        tel=str(input("Digite o telefone do cliente: "))

        sql="INSERT INTO clientes (nome_cliente, email_cliente, tel_cliente) VALUES (%s,%s,%s)"
        cursor=conection.cursor()
        cursor.execute (sql, (nome,email,tel))
        conection.commit()
        cursor.close()
        conection.close()
        print("-----------------------------------------------")
        print("Cadstro de cliente executado com sucesso!")
        print("-----------------------------------------------")

    #opção 5
    elif option == 5:
        print("-----------------------------------------------")
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
        print("-----------------------------------------------")
        print("Cadstro de produto executado com sucesso!")
        print("-----------------------------------------------")

    #opção 6
    elif option == 6:
        print("-----------------------------------------------")
        id_cliente = int(input("Digite o ID do cliente comprador: "))
        id_produto = int(input("Digite o ID do produto a ser comprado: "))
        qntd = int(input("Digite a quantidade de unidades do produto a serem compradas: "))

        # Check if client ID exists
        cursor = conection.cursor()
        cursor.execute("SELECT id_cliente FROM clientes WHERE id_cliente = %s", (id_cliente,))
        client = cursor.fetchone()
        cursor.close()

        if not client:
            print("Erro: Cliente não encontrado.")
            conection.close()
            exit()

        # Check if product ID exists
        cursor = conection.cursor()
        cursor.execute("SELECT id_produto, valor_custo, valor_venda FROM produtos WHERE id_produto = %s", (id_produto,))
        product = cursor.fetchone()
        cursor.close()

        if not product:
            print("Erro: Produto não encontrado.")
            conection.close()
            exit()

        # Insert order into pedidos table
        sql = "INSERT INTO pedidos (id_cliente, id_produto, qntd, custo_pedido, valor_pedido) VALUES (%s,%s,%s,%s,%s)"
        cursor = conection.cursor()
        custo_pedido = product[1] * qntd
        valor_pedido = product[2] * qntd
        cursor.execute(sql, (id_cliente, id_produto, qntd, custo_pedido, valor_pedido))
        conection.commit()
        cursor.close()
        conection.close()
        print("-----------------------------------------------")
        print("Cadstro de produto executado com sucesso!")
        print("-----------------------------------------------")
    
    #opção 7
    elif option == 7:
        print("-----------------------------------------------")
        id_produto_p_mudar_valores=int(input("Digite o ID do produto que deseja mudar o custo e valor de venda: "))
        novo_valor_custo=input("Digite o novo valor de custo do produto (ou pressione Enter para manter o valor atual): ")
        novo_valor_venda=input("Digite o novo valor de venda do produto (ou pressione Enter para manter o valor atual): ")

        cursor=conection.cursor()

        cursor.execute("SELECT id_produto, valor_custo, valor_venda FROM produtos WHERE id_produto = %s", (id_produto_p_mudar_valores,))
        produto = cursor.fetchone()

        if not produto:
            print("Erro: Produto não encontrado.")
            conection.close()
            exit()

        if novo_valor_custo != "":
            novo_valor_custo = float(novo_valor_custo)
            sql_custo="UPDATE produtos SET valor_custo = %s WHERE id_produto = %s"
            cursor.execute (sql_custo, (novo_valor_custo, id_produto_p_mudar_valores))
            conection.commit()

        if novo_valor_venda != "":
            novo_valor_venda = float(novo_valor_venda)
            sql_venda="UPDATE produtos SET valor_venda = %s WHERE id_produto = %s"
            cursor.execute (sql_venda, (novo_valor_venda, id_produto_p_mudar_valores))
            conection.commit()

        cursor.close()
        conection.close()
        print("-----------------------------------------------")
        print(f"Mudança de valores do produto '{id_produto_p_mudar_valores}' executado com sucesso!")
        print("-----------------------------------------------")
    
    #opção 8
    elif option == 8:
        print("-----------------------------------------------")
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
    print(f"Erro ao executar comando: {e}")