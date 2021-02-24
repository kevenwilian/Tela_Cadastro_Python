import pymysql

conexao = pymysql.connect(host= "localhost", user="root", passwd ="",database="tb_redcarautocenter")

cursor = conexao.cursor()
cursor.execute("""CREATE TABLE tb_cadcliente(cpf INT,
                nome VARCHAR(50),
                endereco VARCHAR(50),
                carroemarca VARCHAR(15),
                placa VARCHAR(20),
                PRIMARY KEY tb_cadcliente(cpf));""")

cursor.close()
conexao.close()
