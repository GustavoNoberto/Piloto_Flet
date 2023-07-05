import oracledb

class DatabaseConnection:

    _instance = None

    #Conexao DB
    oracledb.init_oracle_client(lib_dir=r"C:\app\product\instantclient_11_2",
                            config_dir=r"C:\app\product\instantclient_11_2\network\admin")

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
        return cls._instance

    def connect(self):
        # Configuração da conexão com o banco de dados Oracle
        dsn = oracledb.makedsn('rpa-srv-scan.titulo.net', 1521, service_name='rpa.saspsubpro01.saspvcn01.oraclevcn.com')
        username = 'RPA'
        password = 'rp45t4g3'
        self.conn = oracledb.connect(user=username,password=password,dsn=dsn)

    def close(self):
        self.conn.close()

    def commit(self):
        self.conn.commit()
    
    