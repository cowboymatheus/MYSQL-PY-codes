import mysql.connector

try:
    conection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        database="banco"
    )

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

except Exception as e:
    print(f"Erro ao salvar dados: {e}")