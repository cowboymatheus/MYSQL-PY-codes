import mysql.connector
import datetime
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
    print("(7) Modificar Email do Leitor")
    print("(8) Deletar Linha de uma Tabela")
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

    #opção 6 Cadastrar Empréstimo
    elif option == 6:
        print("-----------------------------------------------")
        IdLivroEmprestado = int(input("Digite o ID do livro a ser emprestado: "))
        IdLeitorEmprestador = int(input("Digite o ID do leitor a alugar um livro: "))

        # Checkar se ID do livro existe
        cursor = conection.cursor()
        cursor.execute("SELECT id_livro FROM livros_tb WHERE id_livro = %s", (IdLivroEmprestado,))
        livro = cursor.fetchone()
        cursor.close()

        if not livro:
            print("Erro: Livro não encontrado.")
            conection.close()
            exit()

        # Checkar se ID do leitor existe
        cursor = conection.cursor()
        cursor.execute("SELECT id_leitor FROM leitores_tb WHERE id_leitor = %s", (IdLeitorEmprestador,))
        leitor = cursor.fetchone()
        cursor.close()

        if not leitor:
            print("Erro: Leitor não encontrado.")
            conection.close()
            exit()

        # Calcular data de devolução
        timestampAtual = datetime.datetime.now()
        timestampDevolucao = timestampAtual + datetime.timedelta(days=7)

        # Inserir Empréstimo na tabela Empréstimos
        sql = "INSERT INTO emprestimos_tb (id_livro_emprestimo, id_leitor_emprestimo, data_devolucao) VALUES (%s,%s,%s)"
        cursor = conection.cursor()
        cursor.execute(sql, (IdLivroEmprestado, IdLeitorEmprestador, timestampDevolucao))
        conection.commit()
        cursor.close()
        conection.close()
        print("-----------------------------------------------")
        print("Cadstro de emprestimo executado com sucesso!")
        print("-----------------------------------------------")
    
    #opção 7 Modifucar Email do Leitor
    elif option == 7:
        print("-----------------------------------------------")
        IdLeitorPMudarEmail = int(input("Digite o ID do Leitor que deseja mudar o email: "))
        NovoEmail = input("Digite o novo email do leitor: ")

        cursor=conection.cursor()

        cursor.execute("SELECT email_leitor FROM leitores_tb WHERE id_leitor = %s", (IdLeitorPMudarEmail,))
        leitor = cursor.fetchone()

        if not leitor:
            print("Erro: Produto não encontrado.")
            conection.close()
            exit()

        if NovoEmail != "":
            sql = "UPDATE leitores_tb SET email_leitor = %s WHERE id_leitor = %s"
            cursor.execute (sql, (NovoEmail, IdLeitorPMudarEmail))
            conection.commit()

        cursor.close()
        conection.close()
        print("-----------------------------------------------")
        print(f"Mudança de email do leitor '{IdLeitorPMudarEmail}' executado com sucesso!")
        print("-----------------------------------------------")
    
    #opção 8 Deletar Linha de uma Tabela
    elif option == 8:
        print("-----------------------------------------------")
        print("(1) Deletar linha da tabela 'Livros'")
        print("(2) Deletar linha da tabela 'Leitores'")
        print("(3) Deletar linha da tabela 'Empréstimos'")
        option = int(input(f"Digite o número da sua opção: "))
        id_linha_a_ser_del = int(input(f"Digite o ID da linha que deseja deletar: "))
        cursor=conection.cursor()

        if option == 1:
            print("------------------------------")
            cursor.execute("DELETE FROM livros_tb WHERE id_livro = %s", (id_linha_a_ser_del,))
            conection.commit()
            print("Linha da tabela 'Livros' deletada com sucesso!")
            print("------------------------------")

        elif option == 2:
            print("------------------------------")
            cursor.execute("DELETE FROM leitores_tb WHERE id_leitor = %s", (id_linha_a_ser_del,))
            conection.commit()
            print("Linha da tabela 'Leitores' deletada com sucesso!")
            print("------------------------------")

        elif option == 3:
            print("------------------------------")
            cursor.execute("DELETE FROM emprestimos_tb WHERE id_emprestimo = %s", (id_linha_a_ser_del,))
            conection.commit()
            print("Linha da tabela 'Empréstimos' deletada com sucesso!")
            print("------------------------------")
    
except Exception as e:
    print(f"Erro ao executar comando: {e}")