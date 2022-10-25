#Biblioteca para conexao SSH via Python
from paramiko import SSHClient,AutoAddPolicy

#Classe responsavel conexao SSH
class ConectaSSH():
    def __init__(self,ip):
        self.ip = ip
        self.login = 'root'
        self.senha = ''
        self.ssh = SSHClient()

    #inicia a conexao
    def conectaSSH(self):
        try:
            self.ssh.set_missing_host_key_policy(AutoAddPolicy())
            self.ssh.connect(hostname=self.ip, username=self.login, password=self.senha)
        except: print(f'Erro ao tentar conectar ao IP {self.ip} informado via SSH')

    #Executa o comando informado
    def executaSSH(self,comando):
        stdin, stdout, stderr = self.ssh.exec_command(comando)
        stdin.close()
