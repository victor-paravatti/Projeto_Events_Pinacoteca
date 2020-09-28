from PyQt5 import  uic,QtWidgets
import mysql.connector

conexao = mysql.connector.connect(host='localhost', database='evento', user='root', password='')
cursor = conexao.cursor(prepared=True)

def chama_segunda_tela():

    
    conexao = mysql.connector.connect(host='localhost', database='evento', user='root', password='')
    cursor = conexao.cursor(prepared=True)
    
    primeira_tela.label_4.setText("")
    nome = primeira_tela.lineEdit.text()
    senha = primeira_tela.lineEdit_2.text()
    cursor.execute(f"SELECT senha FROM funcionario WHERE nome = '{nome}'")
    leitura = cursor.fetchall()

    leitura = "".join(leitura[0])

    if len(leitura) == 0:
        primeira_tela.label_4.setText("Dados de login incorretos!")
    elif leitura == senha:
        print("loggin efetuado")
        primeira_tela.close()
        segunda_tela.show()
   

        """  if nome_usuario == "joao123" and senha == "123456" :
        primeira_tela.close()
        segunda_tela.show()"""

    else :
        primeira_tela.label_4.setText(" Senha incorreta!")
    

def logout():
    segunda_tela.close()
    primeira_tela.show()

def abre_tela_cadastro():
    tela_cadastro.show()


def cadastrar(cursor,conexao):
    nome = tela_cadastro.lineEdit.text()
    login = tela_cadastro.lineEdit_2.text()
    senha = tela_cadastro.lineEdit_3.text()
    c_senha = tela_cadastro.lineEdit_4.text()

    if (senha == c_senha):
        try:
            cursor.execute("INSERT INTO funcionario VALUES ('"+nome+"','"+login+"','"+senha+"')")

            conexao.commit() 
            cursor.close()
            tela_cadastro.label.setText("Usuario cadastrado com sucesso")

        except mysql.Error as erro:
            print("Erro ao inserir os dados: ",erro)
    else:
        tela_cadastro.label.setText("As senhas digitadas estão diferentes")
    

    


app=QtWidgets.QApplication([])
primeira_tela=uic.loadUi("primeira_tela.ui")
segunda_tela = uic.loadUi("segunda_tela.ui")
tela_cadastro = uic.loadUi("tela_cadastro.ui")
primeira_tela.pushButton.clicked.connect(chama_segunda_tela)
segunda_tela.pushButton.clicked.connect(logout)
primeira_tela.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
primeira_tela.pushButton_2.clicked.connect(abre_tela_cadastro)
tela_cadastro.pushButton.clicked.connect(cadastrar) 


primeira_tela.show()
app.exec()