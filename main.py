from os import system
from valida_loja import ValidaLoja

#Define o tamanho que ira abrir o prompt
system('mode 70,15')

# Define a cor da letra como verde no prompt
system("color a")


def informacoes():
    #Ip para conexão com Banco MYSQL do PDV
    ip = str(input("Qual o IP da imagem que será configurada?\n"))
    system('cls')
    #Numero da loja que ira receber a imagem usando como exemplo loja 2
    loja = str(input("Para qual loja será enviada essa imagem ?\n"))
    system('cls')
    #numero do pdv usando 3 digitos como por exemplo pdv 001 ou pdv 015
    pdv = str(input("Qual será o numero do PDV?\n")).rjust(3,'0')
    system('cls')
    #Essa variavel alem de ser utilizada para o ip do PDV tb é utilizada na tabela de parametros do banco do PDV
    ippdv = str(input("Qual será o novo IP do PDV?\n"))
    system('cls')


    confirmacao = str(input(f'A imagem sera configurada com as seguintes informações\n\n'
                            f'Loja {loja}\nPDV {pdv}\nIP {ippdv}\nconfirma as informações ?\n\n'
                            f's - SIM\nn - Não\n'))

    if str.upper(confirmacao) == 'S' or str.upper(confirmacao) =='SIM' :
        validacao = ValidaLoja(ip, loja, pdv, ippdv)
        validacao.direcionamento()
    else:
        print('Ok prencha novamente\n')
        informacoes()

informacoes()