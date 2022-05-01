import random
# OWn
import calc

"""
(KEYS MUST FOLLOW THIS STANDARD)
pb --> n, e
pv --> p, q, d

"""

class Keys:

    def __init__(self):
        self.variaveisPseudoaleatorias = self.gerar_variaveis_pseudoaleatorias()
        self.variaviesDeCalculo = self.calcular_vairaveis_de_calculo(self.variaveisPseudoaleatorias[0],
                                                                     self.variaveisPseudoaleatorias[1],
                                                                     self.variaveisPseudoaleatorias[2])
        self.pb = self.g_pb(self.variaviesDeCalculo[0], self.variaveisPseudoaleatorias[2])
        self.pv = self.g_pv(self.variaveisPseudoaleatorias[0], self.variaveisPseudoaleatorias[1],
                            self.variaviesDeCalculo[2])

    @staticmethod
    def gerar_variaveis_pseudoaleatorias():

        # Vars
        p, q, p_diferente_q = None, None, False
        tamanho_da_linha = 7  # all lines of the lp.txt file contain 7 bytes (counting with "\n")
        quantidade_de_linhas = 41637

        caminhoBancoDeDados = '../.glp/lp.txt' if __name__ == '__main__' else './.glp/lp.txt'

        with open(caminhoBancoDeDados) as bd:

            # (p, q)
            while not p_diferente_q:  # This loop ensures that p and q are different
                if p == q:
                    linha_p = random.choice(range(quantidade_de_linhas))  # choice
                    bd.seek(0, 0)  # Reset
                    bd.seek(tamanho_da_linha * linha_p)  # positioning on the chosen line

                    p = int(bd.readline())

                    # Escolha de q
                    linha_q = random.choice(range(quantidade_de_linhas))  # sorteio da linha
                    bd.seek(0, 0)  # Reset
                    bd.seek(tamanho_da_linha * linha_q)  # positioning on the chosen line

                    q = int(bd.readline())
                else:
                    p_diferente_q = True

            # (e)
            e = calc.gerar_e((p - 1) * (q - 1))  # phi equivalent argument

        return p, q, e

    @staticmethod
    def calcular_vairaveis_de_calculo(p, q, e):
        n = calc.n(p, q)
        phi = calc.phi(p, q)
        d = calc.modinv(e, phi)
        return n, phi, d

    @staticmethod
    def g_pb(n, e):
        return n, e

    @staticmethod
    def g_pv(p, q, d):
        return p, q, d

