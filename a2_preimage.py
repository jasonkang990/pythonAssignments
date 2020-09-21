import hashlib, math, string, random, sys

def find_preimage(target,n):
    z = float(n)
    goal = target[0:int(z)]
    st = string.printable
    j = 0
    a = 0
    print(int(z))
    while j == 0:
        a +=1
        m = hashlib.sha256()
        x = ''.join(random.choice(st) for i in range (8))
        m.update(x)
        o = m.digest()
        n = o[0:int(z)]
        if (n == goal):
            j == 1
            return x

