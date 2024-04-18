import mysql.connector

try:
    conection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        database="banco"
    )

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

except Exception as e:
    print(f"Erro ao salvar dados: {e}")