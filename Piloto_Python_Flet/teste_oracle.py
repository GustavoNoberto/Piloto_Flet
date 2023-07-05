import oracledb
import getpass


#oracledb.init_oracle_client()

oracledb.init_oracle_client(lib_dir=r"C:\app\product\instantclient_11_2",
                           config_dir=r"C:\app\product\instantclient_11_2\network\admin")

# Configuração da conexão com o banco de dados Oracle
dsn = oracledb.makedsn('rpa-srv-scan.titulo.net', 1521, service_name='rpa.saspsubpro01.saspvcn01.oraclevcn.com')
username = 'RPA'
password = 'rp45t4g3'

# Estabelece a conexão
connection = oracledb.connect(user=username, password=password, dsn=dsn)

# Cria um cursor para executar comandos SQL
cursor = connection.cursor()

cursor.execute('SELECT * FROM RPA_GERENCIADOR_REMINDERS')
result = cursor.fetchall()
columns=[column[0] for column in cursor.description],
rows=[dict(zip(columns,row)) for row in result]
for row in rows:
    print(row)

cursor.close()
connection.close()
'''

import getpass
import oracledb

#oracledb.init_oracle_client()

oracledb.init_oracle_client(lib_dir=r"C:\app\product\instantclient_11_2",
                           config_dir=r"C:\app\product\instantclient_11_2\network\admin")

#pw = getpass.getpass("Enter password: ")
pw = 'rp45t4g3'

connection = oracledb.connect(
    user="RPA",
    password=pw,
    dsn = oracledb.makedsn('rpa-srv-scan.titulo.net', 1521, service_name='rpa.saspsubpro01.saspvcn01.oraclevcn.com'))
#password = 'rp45t4g3'
print("Successfully connected to Oracle Database")

cursor = connection.cursor()

cursor.close()
connection.close()

'''