from tkinter import *
import pymysql

Menu = Tk()
Menu.title("RedCar Automocenter")
Menu.geometry("400x300")

# Menu cadastro de cliente 
def cadastro():
    cad = Tk()
    cad.geometry("600x600")

    label_titulo = Label(cad, text="CADASTRO CLIENTE",width=40, bg='red', fg='#FFFFFF', font=("Helvetica",30))
    label_titulo.pack(side=TOP, ipady=15)
        
    label_cpf = Label(cad, text="CPF", width=20,)
    label_cpf.place(x=6,y=160)

    cpf = Entry(cad,width=20, font=("Helvetica"))
    cpf.place(x=115,y=160)
        
    label_nome = Label(cad, text="Nome", width=20)
    label_nome.place(x=6,y=210)

    nome = Entry(cad,width=20, font=("Helvetica"))
    nome.place(x=115,y=210)
        
    #label_fone = Label(cad, text="Fone", width=20)
    #label_fone.place(x=6,y=260)

    #fone = Entry(cad,width=20, font=("Helvetica"))
    #fone.place(x=115,y=260) 

    label_endereco = Label(cad, text="Endereço", width=20)
    label_endereco.place(x=6,y=310)

    endereco = Entry(cad,width=20, font=("Helvetica"))
    endereco.place(x=115,y=310)
        
    label_carro_marca = Label(cad, text="Carro/Marca", width=20)
    label_carro_marca.place(x=6,y=360)

    carro_marca = Entry(cad,width=20, font=("Helvetica"))
    carro_marca.place(x=115,y=360)
        
    label_placa = Label(cad, text="Placa", width=20)
    label_placa.place(x=6,y=410)

    placa = Entry(cad,width=20, font=("Helvetica"))
    placa.place(x=115,y=410)

    # BOTOM CADASTRAR CLIENTE QUE CHAMA DEF SALVAR   
    btnsalve = Button(cad,text="Cadastrar",width=20,command=salvar(cpf,nome,endereco,carro_marca,placa,))
    btnsalve.place(x=205,y=520)

# FUNÇÃO SALVAR CLIENTE     
def salvar(cpf,nome,endereco,carro_marca,placa,):   
    #ENTRA NO BANCO DE DADOS PARA SALVAR CLIENTE
    conexao = pymysql.connect(host= "localhost", user="root", passwd ="",database="tb_redcarautocenter")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO tb_cadcliente(cpf,nome,endereco,carroemarca,placa) VALUES(?,?,?,?,?)"
    (cpf,nome,endereco,carro_marca,placa,))
    conexao.commit()
    cursor.close()
    conexao.close()

# Tela inicial do programa 
label1_0 = Label(Menu, text="RED CAR", width=30, bg='red', fg='#FFFFFF', font=("Helvetica", 30))
label1_0.pack(side=TOP, ipady=15)

btncadcliente = Button(Menu, text="Cadastro de Cliente", width=20,command = cadastro)
btncadcliente.place(x=10, y=100)

btnorcamento = Button(Menu, text="Orçamento", width=20)
btnorcamento.place(x=10, y=130)

btncadfuncionario = Button(Menu, text="Cadastro de Cliente", width=20)
btncadfuncionario.place(x=10, y=160)

btngasto = Button(Menu, text="Gasto", width=20)
btngasto.place(x=10, y=190)

Menu.mainloop()
