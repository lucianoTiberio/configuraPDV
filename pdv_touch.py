import dump_ssh
import querys
import scripts_ssh
import time
import os

class PdvTouch():
    def __init__(self,ip, loja, pdv, ippdv):
        self.ip = ip
        self.loja = loja
        self.pdv = pdv
        self.ippdv = ippdv

    def execucao(self):
        print('Configurando......')
        #executa o dump de um PDV da loja solicitada para imagem que esta sendo preparada
        dumpInfLoja = dump_ssh.DumpSSH(self.ip, self.loja)
        dumpInfLoja.mysqldump()
        time.sleep(40)
        #Configura qual sera o concetrador da loja e o seu Jboss
        configuraSSH = scripts_ssh.Scripts(self.ip,self.loja, self.ippdv)
        configuraSSH.concetrador()
        configuraSSH.jboss()
        #Realiza da conguração dos paremetros da loja e pdv nas tabelas do banco
        configuraMysql = querys.ConfiguraMysql(self.ip, self.loja, self.pdv, self.ippdv)
        configuraMysql.controle()
        configuraMysql.pdvParametros()
        configuraMysql.tefParametros()

        #O PDV touch não é configurado em interfaces como o PDV classico e sim no NetworkManager
        configuraSSH.ipNetmanager()
        configuraSSH.gwNetmanager()
        configuraSSH.dnsNetmanager()
        time.sleep(2)
        os.system('cls')
        print('Todas as configurações foram realizadas\nA maquina ira reiniciar e estara pronta para o envio\n')
        configuraSSH.reboot()
        os.system('pause')