import pdv_touch
import pdv_classico
import os

#Define o tamanho que ira abrir o prompt
os.system('mode 55,15')

#Define a cor da letra como verde no prompt
os.system("color a")

def menu():

    #Ip para conexão com Banco MYSQL do PDV
    ip = str(input("Qual o IP da imagem que será configurada?\n"))
    os.system('cls')

    #Numero da loja que ira receber a imagem usando como exemplo loja 2
    loja = str(input("Para qual loja será enviada essa imagem ?\n"))
    os.system('cls')
    #numero do pdv usando 3 digitos como por exemplo pdv 001 ou pdv 015
    pdv = str(input("Qual será o numero do PDV?\n")).rjust(3,'0')
    os.system('cls')
    #Essa variavel alem de ser utilizada para o ip do PDV tb é utilizada na tabela de parametros do banco do PDV
    ippdv = str(input("Qual será o novo IP do PDV?\n"))
    os.system('cls')

    pdvClassico = pdv_classico.PdvClassico(ip,loja,pdv,ippdv)
    pdvTouch = pdv_touch.PdvTouch(ip,loja,pdv,ippdv)

    # Em caso de abertura de novas lojas, sera nescessario incluir as mesmas na lista
    lpdvclassico = [2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 16, 17, 19, 20, 21, 22]
    lpdvtouch = [18, 23]

    # Essa função é reponsavel por verificar qual versão do sistema sera executada.
    def validacao():
        if int(loja) in lpdvclassico:
            pdvClassico.execucao()
        elif int(loja) in lpdvtouch:
            pdvTouch.execucao()
        else:
            print("\nA Loja informada não consta no sistema !\n"
                  "Se for uma loja nova solicite o cadastramento ao desenvolvedor\n"
                  "Em caso de ter digitado a loja errada tente novamente\n\n")
            menu()
    validacao()
menu()
