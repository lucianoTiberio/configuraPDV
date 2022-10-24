import os
import valida_loja

#Define o tamanho que ira abrir o prompt
os.system('mode 70,15')

# Define a cor da letra como verde no prompt
os.system("color a")


def informacoes():
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


    validacao = valida_loja.ValidaLoja(ip,loja,pdv,ippdv)
    validacao.direcionamento()

informacoes()