from math import floor
from math import sqrt
from random import random, randrange


def modulo(a, b):

    if b > 0:
        return round(((a/b) - floor(a/b)) * b)
    else:
        return "integer division by zero is not defined"


def inverse_mult_modulo(a, num):

    if a == (num - 1):
        return -1

    for i in range(1, num):

        if modulo(i * a, num) == 1:
            return i

    return None


def euclide_etendu(dividende, diviseur):
    # initialisation
    x = 1  # x0
    v = 1  # y1
    y = 0  # y0
    u = 0  # x1
    diviseur_pour_inverse = diviseur  # permettra de calculer l'inverse modulaire
    # euclide simple
    while diviseur != 0:
        quotient = dividende // diviseur  # // : floor division
        reste = dividende % diviseur
        dividende = diviseur
        diviseur = reste
    # -----------------------------------
    # euclide etendu
        m = u-quotient*x
        n = v-quotient*y
        u = x
        v = y
        x = m
        y = n
    # ------------------------------------

    # return inverse modulaire
    if diviseur != 0:
        return (v, u, "NULL")
    else:
        return (v, u, v % diviseur_pour_inverse)
        # v: u, v%diviseur_pour_inverse = inverse mult


def exp_rapide(x, pow, n):
    result = 1
    while pow != 0:  # while pow is not zero
        if pow % 2 == 1:  # if the power is even  like n^3
            result = (result * x) % n
        pow = pow // 2  # floor division
        x = (x * x) % n
    return result


def calc_B(p, g, a):
    return exp_rapide(g, a, p)


def calc_y1(p, g, k):
    return exp_rapide(g, k, p)


def calc_y2(m, a, Y, k, p):

    return ((m - (a * Y)) * euclide_etendu(k, (p-1))[2]) % (p - 1)


def verif(m, y, s, A, p, g):

    ay = (A**y * y**s) % p
    if ay == exp_rapide(g, m, p):
        return True
    else:
        return False


def sign(m, a, y, k, p, g):

    return (calc_y2(m, a, y, k, p), calc_y1(p, g, k))


def is_prime(num):

    for i in range(2, floor(sqrt(num))):
        if num % i == 0:
            return False
    return True


def generate_primary_number(start, max):

    lst = list()
    for i in range(start, max):
        rndm = randrange(i, (max))

        if is_prime(rndm) == True:
            lst.append(rndm)

    return lst[len(lst)-1]


def generator_nomber(p):
    lst = list()
    for x in range(2, p):
        for i in range(1, p):
            mo = (x ** i) % p
            if mo not in lst:
                lst.append(mo)

        is_in = True
        for j in range(1, p-1):

            if j not in lst:
                is_in = False
        if is_in == True:
            return lst, x


def pgcd(num1, num2):

    tmp_max = max(num1, num2)
    tmp_min = min(num1, num2)

    while tmp_max % tmp_min > 0:

        tmp = tmp_max
        tmp_max = tmp_min
        tmp_min = tmp % tmp_min
    return tmp_min


def generate_k(p):

    for x in range(int(p/2), p-1):

        if pgcd(x, p-1) == 1:
            return x


# private key
def generate_a(p):
    return randrange(2, (p-2))
