# FUNÇÃO SALVAR CLIENTE     
def salvar():
    # GET PEGA AS INFORMA QUE FOI DIGITADO NOS CAMPOS A CIMA
    salcpf = cpf.get()
    salnome = nome.get()
    salfone = fone.get()
    salendereco = endereco.get()
    salcarro = carro_marca.get()
    salplaca = placa.get()
    
    #ENTRA NO BANCO DE DADOS PARA SALVAR CLIENTE
    conexao = pymysql.connect(host= "localhost", user="root", passwd ="",database="redcarautocenter")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO tb_cadcliente (CPF,NOME,FONE,ENDEREÇO,CARROEMARCA,PLACA)",
    (salcpf,salnome,salfone,salendereco,salcarro,salplaca,))
    conexao.commit()
    cursor.close()
    conexao.close()

# TAMANHO DE TELE DE CADASTROS DE CLIENTE
cad.title("Cadastro de Cliente")
cad.geometry("600x600")
    
