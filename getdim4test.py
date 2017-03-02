import prim_util.prim_util_space_temp as pu
import importlib as imp
import math
import statistics
import time
imp.reload(pu)

#@profile
def randmst(n,trials,d):
    treelen = []
    maxnodes = []
    for i in range(trials):
        nodes,edges = pu.genRandomGraph(n,d)
        res = pu.Prim(nodes,edges,d)
        t = 0
        while any(dist ==math.inf for dist in res):
            t+=.01
            nodes,edges = pu.genRandomGraph(n,d,t,nodes,edges)
            res = pu.Prim(nodes,edges,d)
        treelen.append(sum(res))
        maxnodes.append(max(res))
    print('the average minimum spanning tree weight for a graph with',len(nodes),'nodes in',dimension,'dimensions, over',trials,'trials was:',statistics.mean(treelen))
    return(treelen, maxnodes)

if __name__ == "__main__":
    dimension=3
    values = []
    tree = []
    for nodenum in range(800,801):
        a=time.perf_counter()
        t,m = randmst(nodenum,50,dimension)
        values.append(max(m))
        b=time.perf_counter()
        print(nodenum,b-a)       