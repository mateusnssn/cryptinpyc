import random


def mdc(a, b):
    if b == 0:
        return a
    resto = a % b
    a = b
    b = resto
    return mdc(a, b)



def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y



def modinv(a, m):  # (e, phi) ou --> (number multiplied by d, modulus)
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m



def n(p, q): return p * q



def phi(p, q): return (p-1)*(q-1)



def gerar_e(num):
    while True:
        e = random.randrange(2, num)
        if mdc(num, e) == 1:
            return e
