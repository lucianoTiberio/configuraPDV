from conecta_ssh import ConectaSSH
#Classe responsavel por todos alterações e comando no LINUX
class Scripts():

    def __init__(self,ip,loja, ippdv):
        self.ip = ip
        self.loja = loja
        self.ippdv = ippdv
        self.conexao = ConectaSSH(self.ip)

    def concetrador(self):
        self.conexao.conectaSSH()
        self.comando = f"sed -i 's/192.168.*.100/192.168.{self.loja}.100/' /opt/covabra/prj_PDV/pdv.properties"
        self.conexao.executaSSH(self.comando)

    def jboss(self):

        if int(self.loja) % 2 == 1:
            self.conexao.conectaSSH()
            self.comando = f"sed -i 's/IPJBoss=10.95.7.*/IPJBoss=10.95.7.23/' /opt/covabra/prj_PDV/pdv.properties"
            self.conexao.executaSSH(self.comando)
        else:
            self.conexao.conectaSSH()
            self.comando = f"sed -i 's/IPJBoss=10.95.7.*/IPJBoss=10.95.7.22/' /opt/covabra/prj_PDV/pdv.properties"
            self.conexao.executaSSH(self.comando)

    def ipMaquina(self):
        self.conexao.conectaSSH()
        self.comando = f"sed -i 's/address {self.ip}/address {self.ippdv}/' /etc/network/interfaces"
        self.conexao.executaSSH(self.comando)

    def gwMaquina(self):
        self.conexao.conectaSSH()
        self.comando = f"sed -i 's/gateway 10.95.6.254/gateway 192.168.{self.loja}.254/' /etc/network/interfaces"
        self.conexao.executaSSH(self.comando)

    def dnsMaquina(self):
        self.conexao.conectaSSH()
        self.comando = f"sed -i 's/dns-nameservers 10.95.6.254/dns-nameservers 192.168.{self.loja}.254/' /etc/network/interfaces"
        self.conexao.executaSSH(self.comando)

    def reboot(self):
        self.conexao.conectaSSH()
        self.comando = f"reboot"
        self.conexao.executaSSH(self.comando)

    def ipNetmanager(self):
        self.conexao.conectaSSH()
        self.comando = f"sed -i 's/address1={self.ip}/address1={self.ippdv}/' /etc/NetworkManager/system-connections/'Conexão com cabo.nmconnection'"
        self.conexao.executaSSH(self.comando)

    def dnsNetmanager(self):
        self.conexao.conectaSSH()
        self.comando = f"sed -i 's/dns=10.95.6.254;/dns=192.168.{self.loja}.254;/' /etc/NetworkManager/system-connections/'Conexão com cabo.nmconnection'"
        self.conexao.executaSSH(self.comando)

    def gwNetmanager(self):
        self.conexao.conectaSSH()
        self.comando = f"sed -i 's/,10.95.6.254/,192.168.{self.loja}.254/' /etc/NetworkManager/system-connections/'Conexão com cabo.nmconnection'"
        self.conexao.executaSSH(self.comando)