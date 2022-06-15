

from curses.ascii import isprint
from lib import *
start = 2
end = 10000
m = 42
print("Message: ", m)
p = generate_primary_number(start, end)
print("Nombre premier: ", p)


alpha = generator_nomber(p)[1]
print("Nombre generateur: ", alpha)

a = generate_a(p)
print("clé privée: ", a)

B = calc_B(p, alpha, a)
print("BETA : ", B)

k = generate_k(p)
print("K : ", k)

y1 = calc_y1(p, alpha, k)
y2 = calc_y2(m, a, y1, k, p)

signateur = sign(m, a, y1, k, p, alpha)
print("Signateur : ", signateur)


is_verified = verif(m, y1, y2, B, p, alpha)
print("est-il verifiée ?: ", is_verified)
