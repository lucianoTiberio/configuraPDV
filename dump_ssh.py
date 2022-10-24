import conecta_ssh



class DumpSSH():
    def __init__(self,ip , loja):
        self.ip = ip
        self.loja = loja

        # Essa validação é nescessaria em caso do PDV que vai realizar o DUMP estar desligado ou queimado a possibilidade de todos os PDVs testados estarem deligado ou queimado é muito baixa.
        self.conexao = conecta_ssh.ConectaSSH(f"192.168.{self.loja}.105")
        if self.conexao is not True:
            self.conexao = conecta_ssh.ConectaSSH(f"192.168.{self.loja}.110")
        elif self.conexao is True:
            self.conexao = conecta_ssh.ConectaSSH(f"192.168.{self.loja}.107")
        else:
            self.conexao = self.conexao
    def mysqldump(self):
        self.conexao.conectaSSH()
        self.comando= f'mysqldump -f -u root PDV --add-drop-table controlepdv usuario PDV_PARAMETROS parametrosSAT T_Estabelecimento TEF_PARAMETROS promocaocombomaster promocaocombomasterdetalhe| mysql -u root PDV -h {self.ip}'
        self.conexao.executaSSH(self.comando)

