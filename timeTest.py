from prim_util.prim_util_space_temp import *
import statistics
import sys

n = int(sys.argv[1])
d = int(sys.argv[2])

V,E = genRandomGraph(n,d)

# run with line profiler like this; python kernprof.py -l -v timeTest.py 10000 0
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
            if e[0] in SP:
                if distd[e[0]] > e[1]:
                    distd[e[0]] = e[1]
                    prevd[e[0]] = v[0]
                    H.insert((e[0],distd[e[0]]))
    return (distd.values())


Prim(V,E,d)

