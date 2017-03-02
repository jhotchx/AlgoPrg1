from prim_util.prim_util import *
import statistics
import sys

n = int(sys.argv[1])
d = int(sys.argv[2])


# run with line profiler like this; python kernprof.py -l -v timeTest.py 10000 0
@profile
def Prim(V,E,d):
    if d!=0:
        V = tuple(map(tuple, V))
    SP = set(V)
    distd = dict(zip(V,[math.inf]*len(V)))
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
                    H.insert((e[0],distd[e[0]]))
    return (distd.values())

@profile
def genRandomGraph(n,d,t=0,nodes=None):
    edgedict=defaultdict(list)
    threshold = cutOff(n,d,t)
    if d == 0:
        if nodes is None:
            nodes = range(n)
        for i in range(n-1):
            for j in range(n):
                if j>i:
                    edgewgt = random.random()
                    if edgewgt<threshold:
                        edgedict[i].append([j,edgewgt])
                        edgedict[j].append([i,edgewgt])
    else:
        if nodes is None:
            nodes = [[None]*d]*n
            nodes = [[random.random() for j in nodes[i]] for i in range(n)]
        for i in range(n-1):
            for j in range(n):
                if j>i:
                    itup=tuple(nodes[i])
                    jtup=tuple(nodes[j])
                    edgewgt = euclideanDist(nodes[i],nodes[j])
                    if edgewgt<threshold:
                        edgedict[itup].append([jtup,edgewgt])
                        edgedict[jtup].append([itup,edgewgt])
    return(nodes,edgedict)

V,E = genRandomGraph(n,d)
Prim(V,E,d)

