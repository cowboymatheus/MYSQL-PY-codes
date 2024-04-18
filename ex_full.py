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

    
except Exception as e:
    print(f"Erro ao executar comando: {e}")