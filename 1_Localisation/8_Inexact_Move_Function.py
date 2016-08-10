#Modify the move function to accommodate the added
#probabilities of overshooting or undershooting
#the intended destination.

p=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    U_u = (U - 1) % len(p)
    U_e = U % len(p)
    U_o = (U + 1) % len(p)
    q_u = [x*pUndershoot for x in (p[-U_u:] + p[:-U_u])]
    q_e = [x*pExact for x in (p[-U_e:] + p[:-U_e])]
    q_o = [x*pOvershoot for x in (p[-U_o:] + p[:-U_o])]
    return [sum(vals) for vals in zip(q_u, q_e, q_o)]


print move(p, 1)
