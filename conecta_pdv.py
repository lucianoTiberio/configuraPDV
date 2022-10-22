import mysql.connector

# Classe responsavel por realizar a conexão com banco MYSQL
class ConexaoDB():
    def __init__(self, ip):
        self.host = ip
        self.user = "root"
        self.pwd = ""
        self.db = "PDV"


    def conecta(self):
        try:
            self.con = mysql.connector.connect(
                                                host = self.host,
                                                user = self.user,
                                                password = self.pwd,
                                                database = self.db)
            self.cur = self.con.cursor()
        except: print(f'Erro ao tentar conectar ao banco de dados IP {self.ip} ')

    def desconecta(self):
        self.con.close()

    #Excuta os selects
    def executa_DQL(self, sql):
        self.conecta()
        self.cur.execute(sql)
        res = self.cur.fetchall()
        self.desconecta()
        return res

    #Excuta insert, update...
    def executa_DML(self, sql):
        self.conecta()
        self.cur.execute(sql)
        self.con.commit()
        self.desconecta()


