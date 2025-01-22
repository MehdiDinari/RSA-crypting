import random

def crible(n):
    L = list(range(2, n + 1))
    prem = []
    while len(L) > 0 and (L[0] * L[0]) <= n:
        prem.append(L[0])
        L = [x for x in L if x % L[0] != 0]
    prem.extend(L)  
    return prem

def puis_mod(a, n, m):
    p = 1
    a = a % m
    while n > 0:
        if n % 2 == 1:
            p = (p * a) % m
        a = (a * a) % m
        n //= 2
    return p

def inv_mod(a0, m0):
    a, m, u, s = a0, m0, 1, 0
    while m != 0:
        q, r = divmod(a, m)
        a, m, u, s = m, r, s, u - q * s
    if a == 1:
        while u < 0:
            u += m0
        return u
    else:
        return "a0 n'est pas inversible modulo m0"

def cles():
    p = random.choice(crible(100))
    q = random.choice(crible(100))
    n = p * q
    m = (p - 1) * (q - 1)
    e = random.randint(10, 100)
    while inv_mod(e, m) == "a0 n'est pas inversible modulo m0":
        e = random.randint(10, 100)
    d = inv_mod(e, m)
    return e, d, n

e, d, n = cles()
print(f"e: {e}, d: {d}, n: {n}")