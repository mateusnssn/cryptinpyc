# Own
from RSA import conversion, preCoding, gk


class RSA:
    def __init__(self):
        self.keys = gk.Keys()
        self.pb, self.pv = self.keys.pb, self.keys.pv

    def encrypt(self, dado):
        dado = preCoding.precrypt(dado)
        encrypt = conversion.Encrypt(self.pb, dado)
        return encrypt.dadoCriptografado

    def decrypt(self, dado, pv):
        decrypt = conversion.Decrypt(pv, dado)
        decrypt = preCoding.de_precrypt(decrypt.dadoDecodificado)
        return decrypt
