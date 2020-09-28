def cadastrar_funcionario(conexao, indicador):

    idfuncionario = input("Matricula: ")
    nome = input("Nome: ")
    senha = input("Senha: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    cargo = input("Cargo: ")
    setor = input("Setor: ")

    comando_sql = "INSERT INTO funcionario (idfuncionario, nome, senha, telefone, " \
                  "email, cargo, setor) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    dados = (idfuncionario, nome, senha, telefone, email, cargo, setor)

    indicador.execute(comando_sql, dados)
    conexao.commit()


def cadastar_cliente(conexao, indicador):

    idcpf_cnpj = input("CPF/CNPJ: ")
    nome = input("Nome: ")
    senha = input("Senha: ")
    email = input("E-mail: ")
    data_nascimento = input("Data de Nascimento: ")
    telefone = input("Telefone: ")
    cep = input("Cep: ")
    cidade = input("Cidade: ")
    endereco = input("Endereço: ")
    bairro = input("Bairro: ")

    comando_sql = 'INSERT INTO cliente (idcpf_cnpj, nome, senha, email, ' \
                  'data_nascimento, telefone, cep, cidade, endereco, bairro) ' \
                  'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    dados = (idcpf_cnpj, nome, senha, email, data_nascimento, telefone, cep, cidade, endereco, bairro)

    indicador.execute(comando_sql, dados)
    conexao.commit()


def cadastar_ambiente(conexao, indicador, funcionario=1):

    idambiente = input("Codigo: ")
    localizacao = input("Infome o local: ").upper()
    descricao = input("Informa a descrição: ")
    ocupacao_min = input("Informe a ocupação minima: ")
    ocupacao_max = input("Informe a ocupação máxima: ")
    chv_est_idfuncionario = funcionario

    comando_sql = "INSERT INTO ambiente (idambiente, localizacao, descricao, " \
                  "ocupacao_min, ocupacao_max, idfuncionario) " \
                  "VALUES (%s, %s, %s, %s, %s, %s)"
    dados = (idambiente, localizacao, descricao, ocupacao_min, ocupacao_max, chv_est_idfuncionario)

    indicador.execute(comando_sql, dados)
    conexao.commit()


def cadastar_item(conexao, indicador, funcionario=1, ambiente=2):

    iditem = input("Codigo: ")
    data_inclusao = input("Data: ")
    descricao = input("Descrição: ")
    categoria = input("Categoria: ")
    titulo = input("Título: ")
    tecnica = input("Técnica: ")
    dimencao = input("Dimenção: ")
    autor = input("Autor: ")
    valor = input("Valor: ")
    imagem = input("Imagem: ")
    chv_est_idfuncionario = funcionario
    chv_est_idambiente = ambiente

    comando_sql = "INSERT INTO item (iditem, data_inclusao, descricao, categoria, titulo, " \
                  "tecnica, dimencao, autor, valor, imagem, idfuncionario, idambiente)" \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    dados = (iditem, data_inclusao, descricao, categoria, titulo, tecnica, dimencao,
             autor, valor, imagem, chv_est_idfuncionario, chv_est_idambiente)

    indicador.execute(comando_sql, dados)
    conexao.commit()


def solicitar_locacao(conexao, indicador, cliente=1):

    localizacao = input("Localizacao: ")
    ambiente = input("Ambiente: ")
    tipo_evento = input("Tipo de Evento: ")
    data_evento = input("Data: ")
    formato_evento = input("Formato do Evento: ")
    item = input("Item: ")
    hora_inicial = input("Hora inicial: ")
    hora_final = input("Hora final: ")
    ocupacao = input("Número de convidados: ")
    chv_est_idcpf_cnpj = cliente

    comando_sql = "INSERT INTO solicitacao (localizacao, ambiente, tipo_evento, data_evento, " \
                  "formato_evento, item, hora_inicial, hora_final, ocupacao, idcpf_cnpj)" \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    dados = (localizacao, ambiente, tipo_evento, data_evento, formato_evento,
             item, hora_inicial, hora_final, ocupacao, chv_est_idcpf_cnpj)

    indicador.execute(comando_sql, dados)
    conexao.commit()


def informar_pagamento(conexao, indicador):

    numero_cartao = input("Número Cartão: ")
    titular = input("Titular: ")
    validade = input("Validade: ")
    cvv = input("CVV: ")
    parcelas = input("Parcelas: ")

    comando_sql = "INSERT INTO pagamento (numero_cartao, titular, validade, cvv, parcelas)" \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    dados = (numero_cartao, titular, validade, cvv, parcelas)

    indicador.execute(comando_sql, dados)
    conexao.commit()


def consultar_funcionario(indicador):

    indicador.execute('SELECT idfuncionario, nome, email, telefone, setor, cargo  FROM funcionario')
    leitura = indicador.fetchall()
    print(f"Total de funcionários registrados no sistema: {indicador.rowcount}\n")
    for row in leitura:
        print(f"Matricula: {row[0]}")
        print(f"Nome: {row[1]}")
        print(f"E-mail: {row[2]}")
        print(f"Telefone: {row[3]}")
        print(f"Setor: {row[4]}")
        print(f"Cargo: {row[5]}\n")


def consultar_cliente(indicador):

    indicador.execute('SELECT idcpf_cnpj, nome, email, data_nascimento, '
                      'telefone, cep, cidade, endereco, bairro  FROM cliente')
    leitura = indicador.fetchall()
    print(f"Total de cliente registrados no sistema: {indicador.rowcount}\n")
    for row in leitura:
        print(f"CPF/CNPJ: {row[0]}")
        print(f"Nome: {row[1]}")
        print(f"E-mail: {row[2]}")
        print(f"Data de Nascimento: {row[3]}")
        print(f"Telefone: {row[4]}")
        print(f"Cep: {row[5]}")
        print(f"Cidade: {row[6]}")
        print(f"Endereco: {row[7]}")
        print(f"Bairro: {row[8]}\n")


def consultar_solicitacao(indicador):

    indicador.execute('SELECT idambiente, status_solicitacao FROM solicitacao')
    leitura = indicador.fetchall()
    print(f"Solicitação\n")
    for row in leitura:
        print(f"Ambiente: {row[0]}")
        print(f"Status: {row[1]}")


def responder_solicitacao(indicador):

    indicador.execute("SELECT idambiente, item, ocupacao, hora_inicial, hora_final, "
                      "data_evento FROM solicitacao WHERE status_solicitacao = 'Aguardando Aprovação'")
    leitura = indicador.fetchall()
    print(f"Responder Solicitação\n")
    for row in leitura:
        print(f"Ambiente: {row[0]}")
        print(f"Item: {row[1]}")
        print(f"Quantidade de convidados: {row[2]}")
        print(f"Horário Inicial: {row[3]}")
        print(f"Horário Final: {row[4]}")
        print(f"Data do evento: {row[5]}")


def consultar_ambiente_ocupacao(indicador):

    indicador.execute('SELECT descricao, ocupacao_min, ocupacao_max  FROM ambiente')
    leitura = indicador.fetchall()
    print(f"Consultar Ocupação\n")
    for row in leitura:
        print(f"Ambiente: {row[0]}")
        print(f"Ocupação Minima: {row[1]}")
        print(f"Ocupação Máxima: {row[2]}\n")


def consultar_ambiente_funcionario(indicador):

    indicador.execute('SELECT descricao, idfuncionario  FROM ambiente')
    leitura = indicador.fetchall()
    print(f"Consultar Funcionario\n")
    for row in leitura:
        print(f"Ambiente: {row[0]}")
        print(f"Matricula do funcionario que cadastrou o ambiente: {row[1]}\n")


def login(indicador):

    nome = input("digite usuario: ")
    senha = input("Digite a senha: ")
    indicador.execute(f"SELECT senha FROM funcionario WHERE nome = '{nome}'")
    leitura = indicador.fetchall()

    leitura = "".join(leitura[0])

    if len(leitura) == 0:
        print("Usuario não cadastro")
    elif leitura == senha:
        print("loggin efetuado")


def consultar_item(indicador):

    indicador.execute('SELECT iditem, idfuncionario, idambiente FROM item')
    leitura = indicador.fetchall()
    print(f"Total de Itens registrados no sistema: {indicador.rowcount}\n")
    for row in leitura:
        print(f"Item: {row[0]}")
        print(f"Matricula do funcionario: {row[1]}")
        print(f"Id do Ambiente: {row[2]}")
        

def consultar_solicitacao_pag(indicador):

    indicador.execute('SELECT c.nome,s.idpagamento,s.idfuncionario \
                       FROM solicitacao s  LEFT JOIN cliente c\
                       ON s.idsolicitacao = c.nome\
                       ORDER BY  c.nome')
    leitura = indicador.fetchall()
    print(f"O total de  solicitacões registrados no sistema é: {indicador.rowcount}\n")
    for row in leitura:
        print(f"Nome do cliente: {row[0]}")
        print(f"Numero da ordem de pagamento: {row[1]}")
        print(f"Matricula do funcionario que liberou: {row[2]}")
        print("------------------------------------------\n")


def login_cli(indicador):

    nome = input("digite usuario: ")
    senha = input("Digite a senha: ")
    indicador.execute(f"SELECT senha FROM cliente WHERE nome = '{nome}'")
    leitura = indicador.fetchall()

    leitura = "".join(leitura[0])

    if len(leitura) == 0:
        print("Usuario não cadastro")
    elif leitura == senha:
        print("loggin efetuado")