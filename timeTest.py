from prim_util.prim_util_space_temp import *
import statistics
import sys

n = int(sys.argv[1])
d = int(sys.argv[2])

V,E = genRandomGraph(n,d)

@profile
def Prim(V,E,d):
    if d!=0:
        V = tuple(map(tuple, V))
    SP = set(V)
    distd = dict(zip(V,[math.inf]*len(V)))
    prevd = dict(zip(V,[None]*len(V)))
    distd[V[0]] = 0
    H = minheap()     
    H.insert((V[0],distd[V[0]]))
    while H.heapsize!=-1:
        v = H.delete() 
        if SP:
           SP.remove(v[0])
        for e in E[v[0]]:
            if v[0]==e[0]:
                w = e[1]
            else:
                w = e[0]
            if w in SP:
                if distd[w] > e[2]:
                    distd[w] = e[2]
                    prevd[w] = v[0]
                    H.insert((w,distd[w]))
    return (distd.values())

Prim(V,E,d)

