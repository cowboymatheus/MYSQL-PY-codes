import mysql.connector
try:
    conection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        database="Login_DB"
    )
    
    print("(1) Inserir Usuário")
    print("(2) Deletar Usuário")
    print("(3) Fazer Login")
    option = int(input("Digite o número da sua opção: "))

    #Opção 1 - Inserir Usuário
    if option == 1:
        print("------------------------------------------")
        CPF = int(input("Digite o CPF do usuário: "))
        Nome = str(input("Digite o nome do usuário: "))
        Login = str(input("Digite o login do usuário: "))
        Senha = str(input("Digite a senha do usuário: "))
        Tel = int(input("Digite o telefone do usuário: "))

        sql = "INSERT INTO users_tb (cpf, nome, login, senha, tel) VALUES (%s,%s,%s,%s,%s)"
        cursor = conection.cursor()
        cursor.execute(sql, (CPF, Nome, Login, Senha, Tel))
        conection.commit()
        print("Usuário cadastrado com sucesso!")
        cursor.close()
        conection.close()

    #Opção 2 - Deletar Usuário
    if option == 2:
        print("------------------------------------------")
        Login_A_Ser_Del = str(input("Digite o login do usuário a ser deletado: "))
        Senha_A_Ser_Del = str(input("Digite a senha do usuário a ser deletado: "))

        cursor = conection.cursor()
        cursor.execute("SELECT nome FROM users_tb WHERE login = %s and senha = %s", (Login_A_Ser_Del, Senha_A_Ser_Del))
        Nome = cursor.fetchone()
        cursor.execute("DELETE FROM users_tb WHERE login = %s and senha = %s", (Login_A_Ser_Del, Senha_A_Ser_Del))
        conection.commit()
        print(f"O usuário {Nome}, foi deletado com sucesso!")
        cursor.close()
        conection.close()

    #Opção 3 - Fazer Login
    if option == 3:
        print("------------------------------------------")
        Login = str(input("Digite o seu login: "))
        Senha = str(input("Digite a sua senha: "))

        cursor = conection.cursor()
        cursor.execute("SELECT nome FROM users_tb WHERE login = %s and senha = %s", (Login, Senha))
        Nome = cursor.fetchone()
        conection.commit()
        print(f"Olá {Nome}, Login efetuado com sucesso!")
        cursor.close()
        conection.close()

except Exception as e:
    print(f"Erro ao executar comando: {e}")