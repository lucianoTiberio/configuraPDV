import conecta_pdv


class ConfiguraMysql():
    def __init__(self, ip, loja, pdv, ippdv):
        self.conexao = conecta_pdv.ConexaoDB(ip,'PDV')
        self.loja = loja
        self.pdv = pdv
        self.ippdv = ippdv

    def controle(self):
        self.sql = f"UPDATE controlepdv SET nestab = '{self.loja}', npdv = '{self.pdv}';"
        self.conexao.executa_DML(self.sql)

    def pdvParametros(self):
        self.sql = f"UPDATE PDV_PARAMETROS SET NRPDV = '{self.pdv}', NRECF ='{self.pdv}', IPPDV ='{self.ippdv}', nEstab ='{self.loja}';"
        self.conexao.executa_DML(self.sql)

    def tefParametros(self):
        self.sql = f"UPDATE TEF_PARAMETROS SET NRPDV = '{self.pdv}', IDTERMINAL = 'SE000{self.pdv}',TEF_PARAMETROS.cnpjcontribuinte = (SELECT cnpfContribuinte from parametrosSAT);"
        self.conexao.executa_DML(self.sql)


