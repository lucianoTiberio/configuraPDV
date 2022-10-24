import pdv_touch
import pdv_classico
import time
import os

class ValidaLoja():
    def __init__(self,ip, loja, pdv, ippdv):
        self.ip = ip
        self.loja = loja
        self.pdv = pdv
        self.ippdv = ippdv
        self.lpdvclassico = [2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 16, 17, 19, 20, 21, 22]
        self.lpdvtouch = [18, 23]
        self.pdvClassico = pdv_classico.PdvClassico(self.ip, self.loja, self.pdv, self.ippdv)
        self.pdvTouch = pdv_touch.PdvTouch(self.ip, self.loja, self.pdv, self.ippdv)

    def direcionamento(self):
        if int(self.loja) in self.lpdvclassico:
            self.pdvClassico.execucao()
        elif int(self.loja) in self.lpdvtouch:
            self.pdvTouch.execucao()
        else:
            print(f"\nA Loja {self.loja} informada não consta no sistema !\n"
                  "Se for uma loja nova solicite o cadastramento ao desenvolvedor\n"
                  "\nrevise as informações e tente novamente.\n\n")
            os.system('pause')

