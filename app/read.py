
class Read:
    """
    Receives directory, reads it and returns formatted data for decoding.
    """
    def __init__(self, path):

        self.path = path if path[-1] == '/' else f'{path}/'

        self.dado = self.read_dado()
        self.pb = self.read_pb()
        self.pv = self.read_pv()



        self.hash_l2 = list("0123456789[], ()")
        self.hash_l1 = list("01f3456789harbyk")


        self.dado_traduzido = self.traduzir_dado(self.dado, self.hash_l1, self.hash_l2)
        self.pb_traduzido = self.traduzir_pb(self.pb, self.hash_l1, self.hash_l2)
        self.pv_traduzido = self.traduzir_pv(self.pv, self.hash_l1, self.hash_l2)

    @staticmethod
    def _replace(string, tipo):
        string = string.replace(',', '').replace(')', '').replace('(', '') if tipo == 'tuple' else string.replace(',', '').replace(']', '').replace('[', '')
        return string


    def read_dado(self):
        with open(f'{self.path}ief', 'r+') as file:
            dado = file.read()
        return dado

    def read_pb(self):
        with open(f'{self.path}pb', 'r+') as file:
            pv = file.read()
        return pv

    def read_pv(self):
        with open(f'{self.path}pv', 'r+') as file:
            pv = file.read()
        return pv




    def traduzir_dado(self, dado, hash_l1, hash_l2):
        dado = str(dado)
        for char in dado:
            if dado.count(char) > 0:
                dado = dado.replace(char, str(hash_l2[hash_l1.index(char)]))

        dado = f'{dado}'

        str_formatada = self._replace(dado, 'list').split()
        lista_retorno = []

        for c in list(str_formatada):
            c = int(c)
            lista_retorno.append(c)

        dado = list(lista_retorno)


        return dado


    def traduzir_pb(self, pb, hash_l1, hash_l2):
        pb = str(pb)
        for char in pb:
            if pb.count(char) > 0:
                pb = pb.replace(char, str(hash_l2[hash_l1.index(char)]))
        pb = f'{pb}'

        str_formatada = self._replace(pb, 'tuple').split()
        lista_retorno = []

        for c in list(str_formatada):
            c = int(c)
            lista_retorno.append(c)
        pb = tuple(lista_retorno)



        return pb



    def traduzir_pv(self, pv, hash_l1, hash_l2):
        pv = str(pv)
        for char in pv:
            if pv.count(char) > 0:
                pv = pv.replace(char, str(hash_l2[hash_l1.index(char)]))
        pv = f'{pv}'

        str_formatada = self._replace(pv, 'tuple').split()
        lista_retorno = []

        for c in list(str_formatada):
            c = int(c)
            lista_retorno.append(c)
        pv = tuple(lista_retorno)


        return pv
