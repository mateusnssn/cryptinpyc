
def precrypt(conteudo):
    conteudo = list(conteudo)
    for i in conteudo:
        conteudo[conteudo.index(i)] = ord(i)
    return conteudo


def de_precrypt(conteudo):
    conteudo = conteudo
    for i in conteudo:
        conteudo[conteudo.index(i)] = chr(i)
    return conteudo


if __name__ == '__main__':
    print(precrypt('Loren'))
    print(de_precrypt([76, 111, 114, 101, 110]))
