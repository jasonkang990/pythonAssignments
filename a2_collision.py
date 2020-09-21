import hashlib, math, string, random

def find_collision(n):
    z = float(n)
    st = string.printable
    j = 0
    trials = 0
    arr1 = []
    arr2 = []
    while j == 0:
        trials +=1
        m = hashlib.sha256()
        x = ''.join(random.choice(st) for i in range (8))
        arr2.append(x)
        m.update(x)
        o = m.digest()
        finO = o[0:int(z)]
        arr1.append(finO)
        if (arr1.count(finO) > 1):
            j = 1
            a = arr1.index(finO)
            arr1[a] = None
            b = arr1.index(finO)
            tup = (arr2[a], arr2[b])
            print trials
            return tup
for e in range(0, 15):
    find_collision(2)