import hashlib
from datetime import datetime
import os

class File:
    def __init__(self, pb, pv, dado, path='./', name_dir=None):

        self.path = path
        self.name_dir = name_dir

        self.pb = pb
        self.pv = pv
        self.dado = dado

        self.hash_l1 = list("0123456789[], ()")
        self.hash_l2 = list("01f3456789harbyk")

        self.dadoFormatado = self.gerar_dado_formatado(self.dado, self.hash_l1, self.hash_l2)
        self.pbFormatado = self.gerar_pb_formatado(self.pb, self.hash_l1, self.hash_l2)
        self.pvFormatado = self.gerar_pv_formatado(self.pv, self.hash_l1, self.hash_l2)

        self.name = str(datetime.today())
        self.name = f"{hashlib.md5(self.name.encode('utf-8')).hexdigest()[4:7]}"

        # If the name of the directory is not chosen by the user, it will be named "random"
        if name_dir is None:
            self.path = f'{path if path[-1] == "/" else f"{path}/"}{self.name}'
        else:
            self.path = f'{path if path[-1] == "/" else f"{path}/"}{self.name_dir}'

        os.mkdir(self.path)
        self.path = f'{self.path}/'  # New path to save files


        self.salvar_dado()
        self.salvar_pb()
        self.salvar_pv()

    def gerar_dado_formatado(self, dado, hash_l1, hash_l2):
        dado = str(dado)
        for char in dado:
            if dado.count(char) > 0:
                dado = dado.replace(char, str(hash_l2[hash_l1.index(char)]))

        dado = f'{dado}'
        return dado

    def gerar_pb_formatado(self, pb, hash_l1, hash_l2):
        pb = str(pb)
        for char in pb:
            if pb.count(char) > 0:
                pb = pb.replace(char, str(hash_l2[hash_l1.index(char)]))

        pb = f'{pb}'
        return pb

    def gerar_pv_formatado(self, pv, hash_l1, hash_l2):
        pv = str(pv)
        for char in pv:
            if pv.count(char) > 0:
                pv = pv.replace(char, str(hash_l2[hash_l1.index(char)]))

        pv = f'{pv}'
        return pv




    def salvar_dado(self):
        with open(f'{self.path}/ief', 'w+') as file:
            file.write(self.dadoFormatado)


    def salvar_pb(self):
        with open(f'{self.path}/pb', 'w+') as file:
            file.write(self.pbFormatado)

    def salvar_pv(self):
        with open(f'{self.path}/pv', 'w+') as file:
            file.write(self.pvFormatado)


if __name__ == '__main__':
    test = File((325755551873, 78130628441), (610957, 533189, 139346978633),
                [94333172122, 171896840767], './')
    print(test.dadoFormatado)
    print(test.pbFormatado)
    print(test.pvFormatado)
