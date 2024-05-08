import mysql.connector
try:
    conection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        database="bibliotecaDB"
    )
    
    print("(1) Listar Livros")
    print("(2) Listar Leitores")
    print("(3) Listar Empréstimos")
    print("(4) Cadastrar Livro")
    print("(5) Cadastrar Leitor")
    print("(6) Cadastrar Empréstimo")
    option = int(input(f"Digite o número da sua opção: "))

    #opção 1 Listar Livros
    if option == 1:
        print("-----------------------------------------------")
        cursor=conection.cursor()
        sql = "SELECT * FROM livros_tb"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        conection.commit()
        cursor.close()
        conection.close()

        for resultado in resultados:
            print(f"{resultado}/n")
    
    #opção 2 Listar Leitores
    elif option == 2:
        print("-----------------------------------------------")
        cursor=conection.cursor()
        sql = "SELECT * FROM leitores_tb"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        conection.commit()
        cursor.close()
        conection.close()

        for resultado in resultados:
            print(f"{resultado}/n")
    
    #opção 3 Listar Empréstimos
    elif option == 3:
        print("-----------------------------------------------")
        cursor=conection.cursor()
        sql = "SELECT * FROM emprestimos_tb"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        conection.commit()
        cursor.close()
        conection.close()

        for resultado in resultados:
            print(f"{resultado}/n")

    #opção 4 Cadastrar Livro
    elif option == 4:
        print("-----------------------------------------------")
        TituloLivro = str(input("Digite o título do livro: "))
        AutorLivro = str(input("Digite o autor do livro: "))
        EditoraLivro = str(input("Digite a editora do livro: "))
        EdicaoLivro = str(input("Digite a edição do livro: "))

        sql = "INSERT INTO livros_tb (titulo_livro, autor_livro, editora_livro, edicao_livro) VALUES (%s,%s,%s,%s)"
        cursor = conection.cursor()
        cursor.execute (sql, (TituloLivro, AutorLivro, EditoraLivro, EdicaoLivro))
        conection.commit()
        cursor.close()
        conection.close()
        print("-----------------------------------------------")
        print("Cadstro de livro executado com sucesso!")
        print("-----------------------------------------------")

    #opção 5 Cadastrar Leitor
    elif option == 5:
        print("-----------------------------------------------")
        NomeLeitor = str(input("Digite o nome do leitor: "))
        EmailLeitor= str(input("Digite o email do leitor: "))
        TelLeitor = int(input("Digite o telefone do leitor: "))
        CepLeitor = int(input("Digite o cep do leitor: "))

        sql = "INSERT INTO leitores_tb (nome_leitor, email_leitor, tel_leitor, cep_leitor) VALUES (%s,%s,%s,%s)"
        cursor = conection.cursor()
        cursor.execute (sql, (NomeLeitor, EmailLeitor, TelLeitor, CepLeitor))
        conection.commit()
        cursor.close()
        conection.close()
        print("-----------------------------------------------")
        print("Cadstro de leitor executado com sucesso!")
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
        cursor.close()

        # Update stock quantity in produtos based on quantity sold
        cursor = conection.cursor()
        cursor.execute("UPDATE produtos SET qntd_estoque = qntd_estoque - %s WHERE id_produto = %s", (qntd,id_produto,))
        conection.commit()
        cursor.close()
        conection.close()
        print("-----------------------------------------------")
        print("Cadstro de pedido executado com sucesso!")
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