#Write code that outputs p after multiplying each entry
#by pHit or pMiss at the appropriate places. Remember that
#the red cells 1 and 2 are hits and the other green cells
#are misses.


p=[0.2,0.2,0.2,0.2,0.2]
pHit = 0.6
pMiss = 0.2

#Enter code here
for i in range(0, len(p)):
    pAction = pHit if i in [1,2] else pMiss
    p[i] = p[i] * pAction

print p
