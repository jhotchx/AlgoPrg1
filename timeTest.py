from prim_util.prim_util_space_temp import *
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

def genRandomGraph(n,d,t=0,nodes=None):
    edgedict={}
    threshold=1
    #threshold = cutOff(n,d,t)
    if d == 0:
        if nodes is None:
            nodes = range(n)
        for i in range(n-1):
            for j in range(n):
                if j>i:
                    edge = [i,j,random.random()]
                    if edge[2]<threshold:
                        if i in edgedict:
                            edgedict[i].insert((edge[1],edge[2]))
                        else:
                            edgedict[i] = minheap()
                            edgedict[i].insert(([edge[1],edge[2]]))
                        if j in edgedict:
                            edgedict[j].insert((edge[0],edge[2]))
                        else:
                            edgedict[j] = minheap()
                            edgedict[j].insert(([edge[0],edge[2]]))
    else:
        if nodes is None:
            nodes = [[None]*d]*n
            nodes = [[random.random() for j in nodes[i]] for i in range(n)]
        for i in range(n-1):
            for j in range(n):
                if j>i:
                    itup=tuple(nodes[i])
                    jtup=tuple(nodes[j])
                    edge = [itup,jtup,euclideanDist(nodes[i],nodes[j])]
                    if edge[2]<threshold:
                        if itup in edgedict:
                            edgedict[itup].insert((edge[1],edge[2]))
                        else:
                            edgedict[itup] = minheap()
                            edgedict[itup].insert(([edge[1],edge[2]]))
                        if jtup in edgedict:
                            edgedict[jtup].insert((edge[0],edge[2]))
                        else:
                            edgedict[jtup] = minheap()
                            edgedict[jtup].insert(([edge[0],edge[2]]))
    return(nodes,edgedict)
    
V,E = genRandomGraph(n,d)
Prim(V,E,d)

