from datetime import datetime

import RSA.main as principal
import gfile
import read


def meeting():
    data = str(datetime.today())
    data = data[11:27]
    
    if 7 <= int(data[0:2]) < 12:
        cumprimento = 'Bom dia!'
    elif 12 <= int(data[0:2]) < 18:
        cumprimento = 'Boa tarde!'
    elif 18 <= int(data[0:2]) <= 24 or 0 <= int(data[0:2]) < 7:
        cumprimento = 'Boa noite!'
    else:
        cumprimento = 'Olá'

    space = 30
    print(f'{data.center(space, ".")}\n{"cryptinpyc".center(space)}\n{cumprimento.center(space)}\n{"." * space}\n')
    


def receber_comando(): return input('cryptinpyc >>> ')


def receber_parametro(): return input('[] >>> ')



def ajuda():
    space = 13
    print(f'\n{"- e".ljust(space)}para criptografar')
    print(f'{"- d".ljust(space)}para decodificar')
    print(f'{"- quit".ljust(space)}para sair')
    print(f'{"- help".ljust(space)}para ajuda')



def encrypt():
    print(':::Informe os dados a serem criptografados:::')
    dado = receber_parametro()
    dado = dado.lstrip()

    if dado[0] == '$':
        print("Caminho")
    else:
        e = principal.RSA()
        dadoCriptografado = e.encrypt(dado)
        pb = e.pb
        pv = e.pv
        print(":::Deseja exibir dados gerados?::: (Y/N)")
        resposta = receber_parametro()
        if resposta.upper() == 'Y':
            print(f'DADO CRIPTOGRAFADO................: {dadoCriptografado}')
            print(f'CHAVE PÚBLICA.....................: (n, e) = {pb}')
            print(f'CHAVE PRIVADA.....................: (p, q, d) = {pv}')
        else:
            pass

        print(":::Informe o caminho para salvar o conteúdo:::")
        path = receber_parametro()
        file =  gfile.File(pb, pv, dadoCriptografado, path)



def decrypt():
    print(":::informe o arquivo que pretende decodificar:::")
    path = receber_parametro()
    dadosExtraidos = read.Read(path)
    dado = dadosExtraidos.dado_traduzido
    pv = dadosExtraidos.pv_traduzido
    d = principal.RSA()
    dadoDecodificado = d.decrypt(dado, pv)
    print(f"DADO DECODIFICADO.................: {''.join(dadoDecodificado)}")


# Início
def init():
    meeting()
    print('"help" para ajuda\n')

    # Loop entrada-retorno
    while True:
        comando = receber_comando()
        if comando.upper() == 'HELP':
            ajuda()
        elif comando.upper() == 'E' or comando == 'e':
            encrypt()
        elif comando.upper() == 'D' or comando == 'd':
            decrypt()
        elif comando.upper() == 'EXIT' or comando.upper() == 'QUIT':
            break
        else:
            print('Comando não reconhecido')

if __name__ == '__main__':

    space = 30
    init()
