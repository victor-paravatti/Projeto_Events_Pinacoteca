import events
import mysql.connector
import os
os.system('cls')


conexao = mysql.connector.connect(host='localhost', database='evento', user='root', password='')
cursor = conexao.cursor(prepared=True)
ext = ""

# Laço principal

while ext != "s":

    os.system('cls')    
    opcao = input("Para cadastro de funcionario digite [1]:\
                 \nPara cadastro de Cliente digite [2]: \
                 \nPara Efetuar o Login como Funcionario aperte [3]:\
                 \nPara Efetuar o Login como Cliente aperte [4]:\
                 \n ")

# Opção para  cadastrar o funcionario logar

    if opcao == "1":
        os.system('cls')
        events.cadastrar_funcionario(conexao, cursor)

# Opção para o cadastro do cliente 

    elif opcao == "2":
        os.system('cls')
        events.cadastar_cliente(conexao, cursor)

# Opção para o funcionario logar

    elif opcao == "3":
        os.system('cls')
        events.login(cursor)

        # Opções apos o funcionario logar

        opc = input('\nBem vindo ao Events\n \
                    \n Menu \n\
                    \nPara cadastrar um [Item] aperte [1]: \
                    \nPara cadastrar um [Ambiente] aperte [2]: \
                    \nPara visualizar todos os [Item] cadastrados aperte [3]: \
                    \nPara visualizar todos os [ambientes] cadastrados aperte [4]: \
                    \nPara responder as [Solicitações] aperte [5]: \n') 

        if opc == '1':

            os.system('cls')
            events.cadastar_item(conexao,cursor)
                
        elif opc == '2':

            os.system('cls')
            events.cadastar_ambiente(conexao, cursor)
        elif  opc == '3':

            os.system('cls')
            events.consultar_item(cursor)
                
        elif opc == '4':

            os.system('cls')
            events.consultar_ambiente_ocupacao(cursor)
            events.consultar_ambiente_funcionario(cursor)

        elif opc == '5':

            os.system('cls')
            events.responder_solicitacao(cursor)

# Opção para o funcionario logar

    elif opcao == "4":
        os.system('cls')
        events.login_cli(cursor)
        
      
    ext = input("\nPara sair Digite [s] ou qualquer outra para continuar:  ")
    os.system('cls')
        
        
