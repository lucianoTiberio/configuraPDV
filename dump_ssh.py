import conecta_ssh



class DumpSSH():
    def __init__(self,ip , loja):
        self.ip = ip
        self.loja = loja

        if self.loja == '2':
            self.loja = '1'
        else:
            self.loja = self.loja

        self.conexao = conecta_ssh.ConectaSSH(f"192.168.{self.loja}.105")

    def mysqldump(self):
        self.conexao.conectaSSH()
        self.comando= f'mysqldump -f -u root PDV --add-drop-table controlepdv usuario PDV_PARAMETROS parametrosSAT T_Estabelecimento TEF_PARAMETROS promocaocombomaster promocaocombomasterdetalhe| mysql -u root PDV -h {self.ip}'
        self.conexao.executaSSH(self.comando)

