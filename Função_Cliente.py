import mysql.connector
from mysql.connector import Error, connection, cursor

def conecxao_bd ():
  
    connection = mysql.connector.connect(host='localhost', database='events1', user ='root', password='')
    cursor = connection.cursor()
    print("Conexção feita com sucesso")
    comando_sql = 'INSERT INTO pagamento (cvv, idpagamento, numero_cartao, parcelas, titular, validade) VALUES (%s, %s, %s, %s, %s, %s )'
    dados = ('563', '30', '5499 8507 9095 1557','2', 'victor. g paravatti', '07/28')
    
    cursor.execute(comando_sql, dados)
    
    connection.commit()

    sec_sql = 'SELECT * FROM pagamento'

    cursor.execute(sec_sql)

    valores_lidos = cursor.fetchall()

    print(valores_lidos)
    return cursor
conecxao_bd()   




def fechar_bd ():
    cnx = mysql.connector.connect(user='root', database='events1')
    print("conecxão fechada") 
    return cnx.close()      



"""def cadastro_funcionario ():
    

    conecxao_bd()
    

    comando_sql = 'INSERT INTO pagamento (cvv, idpagamento, numero_cartao, parcelas, titular, validade) VALUES (%s, %s, %s, %s, %s, %s )'
    dados = ('563', '30', '5499 8507 9095 1557','2', 'victor. g paravatti', '07/28')
    
    cursor.execute(comando_sql, dados)
    
    connection.commit()

    sec_sql = 'SELECT * FROM pagamento'

    cursor.execute(sec_sql)

    valores_lidos = cursor.fetchall()

    print(valores_lidos)
    return valores_lidos
    
cadastro_funcionario()"""
"""print("MySQL connection is closed")"""
"""def cadastro_funcionario(matricula, nome, senha, telefone, email, cargo, sertor, )



cursor = mySQLConnection.cursor(buffered=True)
        sql_select_query = 'select * from laptop where id = %s'
        cursor.execute(sql_select_query, (id,))
        record = cursor.fetchall()"""