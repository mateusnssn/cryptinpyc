
class Encrypt:
    def __init__(self, pb, dado):
        self.pb = pb
        self.dado = dado
        self.dadoCriptografado = self.criptografar(self.pb, self.dado)


    @staticmethod
    def criptografar(chave_pb, dado):
        dadoCriptografado = []
        for caractere in dado:
            caractereCriptografado = pow(caractere, chave_pb[1], mod=chave_pb[0])
            dadoCriptografado.append(caractereCriptografado)
        return dadoCriptografado



class Decrypt:
    def __init__(self, pv, dado):
        self.pv = pv
        self.dado = dado
        self.dadoDecodificado = self.decodificar(self.pv, self.dado)


    @staticmethod
    def decodificar(chave_pv, dado):
        n = chave_pv[0] * chave_pv[1]
        dadoPreDecodificado = []
        for caractere in dado:
            caracterePreDecodificado = pow(caractere, chave_pv[-1], n)  # m = (c, d, mod=n)
            dadoPreDecodificado.append(caracterePreDecodificado)
        return dadoPreDecodificado




if __name__ == '__main__':

    """
    pb - (n,e) = (222631833847, 149206200581)
    pv - (p, q, d) = (558791, 398417, 150760677421)
    phi = 222630876640
    d * e = 22494427875005163781601
    dadoCriptografado = [148418125426, 127705656928]
    """

    testeE = Encrypt((222631833847, 149206200581), [12, 13])
    print(testeE.dadoCriptografado)
    testeD = Decrypt((558791, 398417, 150760677421), [148418125426, 127705656928])
    print(testeD.dadoDecodificado)