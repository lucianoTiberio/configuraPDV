from pdv_touch import PdvTouch
from pdv_classico import PdvClassico
from os import system
from conecta_pdv import ConexaoDB

class ValidaLoja():
    def __init__(self,ip, loja, pdv, ippdv):
        self.ip = ip
        self.loja = loja
        self.pdv = pdv
        self.ippdv = ippdv
        self.pdvClassico = PdvClassico(self.ip, self.loja, self.pdv, self.ippdv)
        self.pdvTouch = PdvTouch(self.ip, self.loja, self.pdv, self.ippdv)
        self.conexao = ConexaoDB('10.95.7.28','statuspdv')


    def direcionamento(self):
        self.conexao.conecta()
        self.lpdvclassico = str(self.conexao.executa_DQL("SELECT loja FROM tipo_pdv WHERE touch = 'N'"))
        self.lpdvtouch = str(self.conexao.executa_DQL("SELECT loja FROM tipo_pdv WHERE touch = 'S'"))


        if str(self.loja) in self.lpdvclassico:
            self.pdvClassico.execucao()
        elif str(self.loja) in self.lpdvtouch:
            self.pdvTouch.execucao()
        else:
            print(f"\nA Loja {self.loja} informada não consta no sistema !\n"
                  "Se for uma loja nova solicite o cadastramento ao desenvolvedor\n"
                  "\nrevise as informações e tente novamente.\n\n")
            system('pause')

